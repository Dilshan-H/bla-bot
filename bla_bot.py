#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# Built using python-telegram-bot v20.0a2 and its dependencies.
# Special thanks to python-telegram-bot v20.0a2 example scripts.

"""
Usage:
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import os
from typing import Optional, Tuple
from uuid import uuid4
from html import escape

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        "This bot is only compatible with python-telegram-bot v20.0a2 or higher."
    )


from telegram import (
    Chat,
    ChatMember,
    ChatMemberUpdated,
    Update,
    InlineQueryResultArticle,
    InputTextMessageContent,
)
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    ChatMemberHandler,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
    InlineQueryHandler,
    ConversationHandler,
)

from gpa_values import get_gpa

# Enable logging
logging.basicConfig(
    # filename="app.log",
    # filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

# BOT INFO
BOT_VERSION: str = "0.1.0"
BOT_NAME: str = "TEMP BOT"
BOT_DESCRIPTION: str = """Born on: 2022.08.20 in Sri Lanka.\n
And, Hey, I'm an open-source bot written in Python.
So you can see inside me literally! - How I handle all your requests...\n
Btw If you want, you can copy my source code and make your own bot under MIT license.\n
Also, reporting bugs is always appreciated and pull requests are always welcome! 🤗\n"""


# Choices Data
USER_ID, USER_NIC = range(2)


def extract_status_change(
    chat_member_update: ChatMemberUpdated,
) -> Optional[Tuple[bool, bool]]:
    """
    Takes a ChatMemberUpdated instance and extracts whether the 'old_chat_member' was a member
    of the chat and whether the 'new_chat_member' is a member of the chat. Returns None, if
    the status didn't change.
    """
    status_change = chat_member_update.difference().get("status")
    old_is_member, new_is_member = chat_member_update.difference().get(
        "is_member", (None, None)
    )

    if status_change is None:
        return None

    old_status, new_status = status_change
    was_member = old_status in [
        ChatMember.MEMBER,
        ChatMember.OWNER,
        ChatMember.ADMINISTRATOR,
    ] or (old_status == ChatMember.RESTRICTED and old_is_member is True)
    is_member = new_status in [
        ChatMember.MEMBER,
        ChatMember.OWNER,
        ChatMember.ADMINISTRATOR,
    ] or (new_status == ChatMember.RESTRICTED and new_is_member is True)

    return was_member, is_member


async def track_chats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Tracks the chats the bot is in."""
    result = extract_status_change(update.my_chat_member)
    if result is None:
        return
    was_member, is_member = result

    # Check who is responsible for the change
    cause_name = update.effective_user.full_name

    # Handle chat types differently:
    chat = update.effective_chat
    if chat.type == Chat.PRIVATE:
        if not was_member and is_member:
            logger.info("%s started the bot", cause_name)
            context.bot_data.setdefault("user_ids", set()).add(chat.id)
        elif was_member and not is_member:
            logger.info("%s blocked the bot", cause_name)
            context.bot_data.setdefault("user_ids", set()).discard(chat.id)
    elif chat.type in [Chat.GROUP, Chat.SUPERGROUP]:
        if not was_member and is_member:
            logger.info("%s added the bot to the group %s", cause_name, chat.title)
            context.bot_data.setdefault("group_ids", set()).add(chat.id)
        elif was_member and not is_member:
            logger.info("%s removed the bot from the group %s", cause_name, chat.title)
            context.bot_data.setdefault("group_ids", set()).discard(chat.id)
    else:
        if not was_member and is_member:
            logger.info("%s added the bot to the channel %s", cause_name, chat.title)
            context.bot_data.setdefault("channel_ids", set()).add(chat.id)
        elif was_member and not is_member:
            logger.info(
                "%s removed the bot from the channel %s", cause_name, chat.title
            )
            context.bot_data.setdefault("channel_ids", set()).discard(chat.id)


async def greet_chat_members(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Greets new users in chats and announces when someone leaves"""
    result = extract_status_change(update.chat_member)
    if result is None:
        return

    was_member, is_member = result
    cause_name = update.chat_member.from_user.mention_html()
    member_name = update.chat_member.new_chat_member.user.mention_html()

    if not was_member and is_member:
        await update.effective_chat.send_message(
            f"{member_name} was added by {cause_name}.\nWelcome {member_name}! 🤗 🎉\n\n"
            "I'm {BOT_NAME} btw. If you like to know what can I do, just type /help.",
            parse_mode=ParseMode.HTML,
        )
    elif was_member and not is_member:
        await update.effective_chat.send_message(
            f"{member_name} is no longer with us... See you soon {member_name}! 🙌",
            parse_mode=ParseMode.HTML,
        )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show 'About' section for the bot when the command /help is issued."""
    await update.message.reply_text(
        "<b>Hello there! 👋 I'm TEMP BOT and I'm here for you <i>24x7</i> no matter what 😊</b>"
        "\n\n"
        "<b><u>Basic Commands</u></b>"
        "\n\n"
        "/whois - 😎 Get to know about someone"
        "\n"
        "/help - 👀 Show this message"
        "\n"
        "/about - ⭐ Read about me"
        "\n"
        "/version - 📝 Show the version of the bot"
        "\n\n"
        "<b><u>Academic Related</u></b>"
        "\n\n"
        "/gpa - 📊 Show your GPA data"
        "\n"
        "/uom - 🎓 About UoM"
        "\n"
        "/staff - 👥 Get Staff Info",
        parse_mode=ParseMode.HTML,
    )


async def about_bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show BOT_VERSION & info when the command /about is issued."""
    logger.info("BOT info requested")
    await update.message.reply_text(
        f"I'm {BOT_NAME} - Version {BOT_VERSION} 🤩"
        "\n"
        f"{BOT_DESCRIPTION}"
        "\n\n"
        "Made with ❤️ by <a href='https://github.com/dilshan-h'>@Dilshan-h</a>",
        parse_mode=ParseMode.HTML,
    )


async def about_uom(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show BOT_VERSION & info when the command /about is issued."""
    logger.info("About UoM requested")
    await update.message.reply_text(
        "University of Moratuwa, a leading technological university in the region "
        "welcomes you to witness a truly unique experience!\n"
        "Read More <a href='https://uom.lk/about-the-university'>here.</a>\n\n"
        "<b>📞 General Numbers:</b> 0112640051, 0112650301\n\n"
        "<b>📠 General Fax:</b> +94112650622\n\n"
        "<b>📨 Email:</b> info@uom.lk\n\n"
        "<b>🏬 Address:</b> University of Moratuwa, Bandaranayake Mawatha, Moratuwa 10400\n",
        parse_mode=ParseMode.HTML,
    )


async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the inline query. This is run when you type: @botusername <query>"""
    query = update.inline_query.query

    if query == "":
        return

    results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Capitalize Text",
            input_message_content=InputTextMessageContent(query.upper()),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Bold Text",
            input_message_content=InputTextMessageContent(
                f"<b>{escape(query)}</b>", parse_mode=ParseMode.HTML
            ),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Italic Text",
            input_message_content=InputTextMessageContent(
                f"<i>{escape(query)}</i>", parse_mode=ParseMode.HTML
            ),
        ),
    ]

    await update.inline_query.answer(results)


async def gpa(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Stores the info about the user and ends the conversation."""
    # user = update.message.from_user
    await update.message.reply_text(
        "Okay... Let's see how much you have scored! 🔥\n"
        "Please enter your UoM admission number:\n\n"
        "If you want to cancel this conversation anytime, just type /cancel."
    )
    logger.info("/gpa - Getting user's ID")
    return USER_ID


async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Stores the info about the user and ends the conversation."""
    # user = update.message.from_user
    if get_gpa(update.message.text, 1) != []:
        await update.message.reply_text("Please enter your NIC number")
        logger.info("/gpa - Getting user's NIC")
        return USER_NIC
    else:
        await update.message.reply_text(
            "Invalid ID detected! - Terminating process...\n"
            "Check your ID and try again with command /gpa"
        )

        return ConversationHandler.END


async def get_nic(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Stores the info about the user and ends the conversation."""
    user = update.message.from_user
    logger.info("Received NIC from %s: %s", user.first_name, update.message.text)

    await update.message.reply_text(
        calculate_gpa(update.message.text), parse_mode=ParseMode.HTML
    )

    return ConversationHandler.END


def calculate_gpa(user_nic: str) -> str:
    """Stores the info about the user and ends the conversation."""
    logger.info("Calculating GPA for %s", user_nic)
    results = get_gpa(user_nic, 2)
    message_body: str = ""
    warnings: str = ""

    if results == []:
        return "Invalid NIC detected! - Sorry, You are not authorized to continue..."
    if results[10]:
        return (
            "I can't validate your NIC because it's not registered in database.\n"
            "Please mention admin to update your NIC"
        )

    count: int = 1
    # Semester GPAs
    for item in results[2:10]:
        if item in ["", "\n"]:
            count += 1
            continue
        sgpa: float = round(float(item), 2)
        if sgpa < 1.50:
            warnings += (
                f"🔴 Semester {count} GPA: <b>{sgpa}</b> - <b>Academic Probation</b>\n"
            )
        if sgpa < 2.00:
            warnings += (
                f"🔴 Semester {count} GPA: <b>{sgpa}</b> - <b>Academic Warning</b>\n"
            )
        message_body += f"Semester {count} GPA: <b>{sgpa}</b>\n"
        count += 1
    message_body += "\n"

    # Level GPAs
    for item in results[11:15]:
        if item in ["", "\n"]:
            count += 1
            continue
        message_body += f"Level {count} GPA: <b>{round(float(item), 2)}</b>\n"
        count += 1
    message_body += "\n"

    # Current GPA
    cgpa: float = round(float(results[15]), 2)
    message_body += f"Your Current GPA: <b>{cgpa}</b>\n\n"

    # Academic Status
    if cgpa >= 3.70:
        message_body += (
            "Congrats! 🎉✨ You currently have a First Class 🔥🔥🔥 - Keep it up!"
        )
    elif cgpa >= 3.30:
        message_body += (
            "Congrats! 🎉✨ You currently have a Second Class Upper 🔥🔥 - Keep it up!"
        )
    elif cgpa >= 3.30:
        message_body += (
            "Congrats! 🎉✨ You currently have a Second Class Lower 🔥🔥 - Keep it up!"
        )
    elif cgpa >= 2.00:
        message_body += "Pass! ✨ - Keep it up! - You can achieve a class! 🔥"
    else:
        message_body += "GPA is less than 2.0 😢 - or did I make any mistake?"

    return message_body


async def cancel_conversation(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text("OK, Your request has been cancelled")

    return ConversationHandler.END


async def unknown_commands(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Reply to unknown commands."""
    logger.warning("Unknown command received: %s", update.message.text)
    await update.message.reply_text(
        "Sorry, I didn't understand that command 🤖\nTry /help to see what I can do."
    )


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    # Use environment variables to avoid hardcoding your bot's token.
    application = Application.builder().token(os.environ["TELEGRAM_TOKEN"]).build()

    # Handle members joining/leaving chats.
    application.add_handler(
        ChatMemberHandler(greet_chat_members, ChatMemberHandler.CHAT_MEMBER)
    )
    logger.info("Greeting handler added")

    # Handle '/help' command.
    application.add_handler(CommandHandler("help", help_command))
    logger.info("Help handler added")

    # Handle '/about' command.
    application.add_handler(CommandHandler("about", about_bot))
    logger.info("About handler added")

    # Handle '/uom' command.
    application.add_handler(CommandHandler("uom", about_uom))
    logger.info("About UOM handler added")

    # Handle conversation.
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("gpa", gpa)],
        states={
            USER_ID: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_id)],
            USER_NIC: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_nic)],
        },
        fallbacks=[CommandHandler("cancel", cancel_conversation)],
    )
    application.add_handler(conv_handler)

    # Handle unknown commands.
    application.add_handler(MessageHandler(filters.COMMAND, unknown_commands))
    logger.info("Unknown Command handler added")

    # Handle inline queries.
    application.add_handler(InlineQueryHandler(inline_query))

    # Run the bot until the user presses Ctrl-C
    # Pass 'allowed_updates' handle *all* updates including `chat_member` updates
    # To reset this, simply pass `allowed_updates=[]`
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
