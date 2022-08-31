#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# Built using python-telegram-bot v20.0a2 and its dependencies.
# Special thanks to python-telegram-bot v20.0a2 example scripts.

"""
Usage:
- Make sure to install the dependencies first and configure the BOT INFO, CHAT/TELEGRAM INFO,
TIMEZONE DATA and UNIVERSITY INFO.
- The data files must be formatted as requested.
- Following environment variables are used to configure the bot.
    TELEGRAM_TOKEN -> Telegram bot token.
    DEV_CHAT_ID -> The chat id of the developer where the bot will send debug messages.
    GROUP_CHAT_ID -> The chat id of your group.

Press Ctrl-C on the command line to stop the bot.

Project Name: BLA-20 Bot
Author: @dilshan-h (https://github.com/dilshan-h)
"""

import logging
import traceback
import json
import os
from typing import Optional, Tuple, Union, List
from html import escape
from datetime import time
import pytz

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
)
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    ChatMemberHandler,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler,
)

from gpa_values import calculate_gpa, get_gpa
from staff_info import employee_info
from about_user import user_info
from manage_bdays import generate_wish

# Enable logging
# You can also enable logging to file - Just uncomment below lines
logging.basicConfig(
    # filename="app.log",
    # filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

# BOT INFO
BOT_VERSION: str = "1.6.0"
BOT_NAME: str = "TEMP BOT"
BOT_DESCRIPTION: str = """Born on: 2022.08.20 in Sri Lanka.\n
And, Hey, I'm an open-source bot written in Python.
So you can see inside me literally! - How I handle all your requests...\n
Btw If you want, you can copy my source code and make your own bot under MIT license.\n
Also, reporting bugs is always appreciated and pull requests are always welcome! 🤗\n"""

# CHAT/TELEGRAM INFO
TELEGRAM_TOKEN: str = os.environ["TELEGRAM_TOKEN"]
DEV_CHAT_ID: str = os.environ["DEV_CHAT_ID"]
GROUP_CHAT_ID: str = os.environ["GROUP_CHAT_ID"]

# TIMEZONE DATA
TIME_ZONE: str = "Asia/Colombo"

# UNIVERSITY INFO
UNI_NAME_LONG: str = "University of Moratuwa"
UNI_NAME_SHORT: str = "UoM"
UNI_DESCRIPTION: str = (
    "University of Moratuwa, a leading technological university in the region "
    "welcomes you to witness a truly unique experience!\n"
    "Read More <a href='https://uom.lk/about-the-university'>here.</a>\n\n"
    "<b>📞 General Numbers:</b> 0112640051, 0112650301\n\n"
    "<b>📠 General Fax:</b> +94112650622\n\n"
    "<b>📨 Email:</b> info@uom.lk\n\n"
    "<b>🏬 Address:</b> University of Moratuwa, Bandaranayake Mawatha, Moratuwa 10400\n"
)

# CHOICES DATA
USER_ID, USER_NIC = range(2)
QUERY_STAFF = range(1)
QUERY_USER = range(1)


def authenticate_origin(update: Update) -> bool:
    """
    Checks if the update originated from the group chat.
    """
    return str(update.message.chat.id) == GROUP_CHAT_ID


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


async def check_bdays(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Check for birthdays and send wishes for users"""
    job = context.job
    bday_wishes: List[str] = generate_wish()

    for wish in bday_wishes:
        await context.bot.send_message(
            chat_id=job.chat_id, text=wish, parse_mode=ParseMode.HTML
        )


def remove_task_if_exists(name: str, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """Remove task with given name. Returns whether task was removed."""
    current_tasks = context.job_queue.get_jobs_by_name(name)

    if not current_tasks:
        return False
    for task in current_tasks:
        task.schedule_removal()

    return True


async def manage_scheduled_tasks(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Manage Scheduled tasks"""
    chat_id = update.effective_message.chat_id
    user_id = update.effective_user.id

    if str(user_id) != os.environ["DEV_CHAT_ID"]:
        await update.message.reply_text(
            "⛔ Sorry, You are not authorized to use this command."
        )
        return
    if not authenticate_origin(update):
        # Prevent accidental usage by developers
        await update.message.reply_text(
            "⛔ Request Rejected! - This command requires elevated privileges.\n"
            "Reason: Originated from unrecognized chat id.\n\n"
            "Please visit https://github.com/dilshan-h/bla-bot to make your own bot."
        )
        return
    try:
        state = context.args[0].lower()
    except IndexError:
        await update.message.reply_text("You have to specify a state. [on/off]")
        return
    start_time = time(0, 0, 0, tzinfo=pytz.timezone(TIME_ZONE))

    if state == "on":
        remove_task_if_exists(str(chat_id), context)
        context.job_queue.run_daily(
            check_bdays, start_time, chat_id=chat_id, name=str(chat_id), data=state
        )
        await update.message.reply_text("✅ Scheduled tasks are now enabled!")
    elif state == "off":
        job_removed = remove_task_if_exists(str(chat_id), context)
        text = (
            "❎ Scheduled tasks are now disabled!"
            if job_removed
            else "🚫 No active scheduled tasks!"
        )
        await update.message.reply_text(text)

    else:
        await update.message.reply_text("🚫 Invalid state! [on/off supported]")
        return


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show 'Help' section for the bot when the command /help is issued."""
    await update.message.reply_text(
        f"<b>Hello there! 👋 I'm {BOT_NAME} and I'm here for you <i>24x7</i> no matter what 😊</b>"
        "\n\n"
        "<b><u>Basic Commands</u></b>"
        "\n\n"
        "/whois - 😎 Get to know about someone"
        "\n"
        "/help - 👀 Show this message"
        "\n"
        "/about - ⭐ Read about me"
        "\n\n"
        "<b><u>Academic Related</u></b>"
        "\n\n"
        "/gpa - 📊 Show your GPA data"
        "\n"
        "/staff - 👥 Get Staff Info"
        "\n"
        f"/{UNI_NAME_SHORT.lower()} - 🎓 About {UNI_NAME_SHORT}"
        "\n\n"
        "<b><u>Other</u></b>"
        "\n\n"
        "/tasks - 🕒 Manage scheduled tasks",
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
        "Made with ❤️ by <a href='https://github.com/dilshan-h'>@Dilshan-h</a>"
        "\n\n"
        "Review my source code <a href='https://github.com/dilshan-h'>@GitHub</a>",
        parse_mode=ParseMode.HTML,
    )


async def about_university(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show university info when the command /{UNI_NAME_SHORT} is issued."""
    logger.info("About University Info requested")
    await update.message.reply_text(
        UNI_DESCRIPTION,
        parse_mode=ParseMode.HTML,
    )


async def gpa(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Initiate /gpa conversation & get user's University ID"""
    if not authenticate_origin(update):
        await update.message.reply_text(
            "⛔ Request Rejected! - This command requires elevated privileges.\n"
            "Reason: Originated from unrecognized chat id.\n\n"
            "Please visit https://github.com/dilshan-h/bla-bot to make your own bot."
        )
        return
    await update.message.reply_text(
        "Okay... Let's see how much you have scored! 🔥😋\n"
        f"Please enter your {UNI_NAME_SHORT} admission number:\n\n"
        "If you want to cancel this conversation anytime, just type /cancel."
    )
    logger.info("/gpa - Getting user's ID")
    return USER_ID


async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> Union[str, int]:
    """Run validation on User ID & then request NIC info."""
    if get_gpa(update.message.text, 1) != []:
        await update.message.reply_text("Please enter your NIC number")
        logger.info("/gpa - Getting user's NIC")
        return USER_NIC

    await update.message.reply_text(
        "Invalid ID detected! - Terminating process...\n"
        "Check your ID and try again with command /gpa"
    )

    return ConversationHandler.END


async def get_nic(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Get the user's NIC and call calculate_gpa function. Then return the GPA info
    and end the conversation.
    """
    user = update.message.from_user
    logger.info("Received NIC from %s: %s", user.first_name, update.message.text)

    await update.message.reply_text(
        calculate_gpa(update.message.text), parse_mode=ParseMode.HTML
    )

    return ConversationHandler.END


async def staff(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Get user's search query"""
    await update.message.reply_text(
        "Okay... Let's see who you are looking for! 🧐\n"
        "Please enter your search query (Part of a name, Post, Phone...):\n\n"
        "If you want to cancel this conversation, just type /cancel."
    )
    return QUERY_STAFF


async def get_staff_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Return info about a staff member based on user's query."""
    await update.message.reply_text(
        employee_info(update.message.text), parse_mode=ParseMode.HTML
    )

    return ConversationHandler.END


async def whois(update: Update, context: ContextTypes.DEFAULT_TYPE) -> Union[None, str]:
    """Show information about a specific user."""
    if not authenticate_origin(update):
        await update.message.reply_text(
            "⛔ Request Rejected! - This command requires elevated privileges.\n"
            "Reason: Originated from unrecognized chat id.\n\n"
            "Please visit https://github.com/dilshan-h/bla-bot to make your own bot."
        )
        return
    await update.message.reply_text(
        "Okay... Let's see who you are looking for! 🧐\n"
        "Please enter your search query (Part of a name, email, Phone...):\n\n"
        "If you want to cancel this conversation, just type /cancel.",
        parse_mode=ParseMode.HTML,
    )
    return QUERY_USER


async def get_user_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Return info about a user based on user's query."""
    user = update.message.from_user
    logger.info(
        "WhoIs Info requested by: %s - Request: %s",
        user.first_name,
        update.message.text,
    )
    await update.message.reply_text(
        user_info(update.message.text), parse_mode=ParseMode.HTML
    )

    return ConversationHandler.END


async def cancel_conversation(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> int:
    """Cancels and ends the active conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text("✅ OK, Your request has been cancelled")

    return ConversationHandler.END


async def unknown_commands(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Reply to unknown commands."""
    logger.warning("Unknown command received: %s", update.message.text)
    await update.message.reply_text(
        "Sorry, I didn't understand that command 🤖\nTry /help to see what I can do."
    )


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log the error and send a telegram message to notify the developer."""
    logger.error("Exception while handling an update")

    tb_list = traceback.format_exception(
        None, context.error, context.error.__traceback__, 5
    )
    tb_string = "".join(tb_list)

    update_str = update.to_dict() if isinstance(update, Update) else str(update)

    message = (
        f"🔴 <b><u>{BOT_NAME} - Error Report</u></b>\n\n"
        "An exception was raised while handling an update\n\n"
        f"<pre>update = {escape(json.dumps(update_str, indent=2, ensure_ascii=False))}"
        "</pre>\n\n"
        f"<pre>context.chat_data = {escape(str(context.chat_data))}</pre>\n\n"
        f"<pre>context.user_data = {escape(str(context.user_data))}</pre>\n\n"
        f"⏩ <pre>{escape(tb_string)}</pre>"
    )

    await update.message.reply_text(
        "Oops! Something's wrong 🤖\n"
        "An error occurred while handling your request.\n"
        "The error has been reported to the developer and will be fixed soon.\n"
    )
    await context.bot.send_message(
        chat_id=DEV_CHAT_ID, text=message, parse_mode=ParseMode.HTML
    )


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    # Use environment variables to avoid hardcoding your bot's token.
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Handle members joining/leaving chats.
    application.add_handler(
        ChatMemberHandler(greet_chat_members, ChatMemberHandler.CHAT_MEMBER)
    )
    logger.info("Greeting handler added")

    # Handle scheduled tasks.
    application.add_handler(CommandHandler("tasks", manage_scheduled_tasks))
    logger.info("Scheduled tasks handler added")

    # Handle '/help' command.
    application.add_handler(CommandHandler("help", help_command))
    logger.info("Help handler added")

    # Handle '/about' command.
    application.add_handler(CommandHandler("about", about_bot))
    logger.info("About handler added")

    # Handle '/{UNI_NAME_SHORT}' command.
    application.add_handler(CommandHandler(UNI_NAME_SHORT.lower(), about_university))
    logger.info("About University handler added")

    # Handle conversation - GPA Info
    gpa_conv_handler = ConversationHandler(
        entry_points=[CommandHandler("gpa", gpa)],
        states={
            USER_ID: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_id)],
            USER_NIC: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_nic)],
        },
        fallbacks=[CommandHandler("cancel", cancel_conversation)],
    )
    application.add_handler(gpa_conv_handler)

    # Handle conversation - Staff Info
    staff_conv_handler = ConversationHandler(
        entry_points=[CommandHandler("staff", staff)],
        states={
            QUERY_STAFF: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, get_staff_info)
            ],
        },
        fallbacks=[CommandHandler("cancel", cancel_conversation)],
    )
    application.add_handler(staff_conv_handler)

    # Handle conversation - User Info
    user_conv_handler = ConversationHandler(
        entry_points=[CommandHandler("whois", whois)],
        states={
            QUERY_USER: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, get_user_info)
            ],
        },
        fallbacks=[CommandHandler("cancel", cancel_conversation)],
    )
    application.add_handler(user_conv_handler)

    # Handle unknown commands.
    application.add_handler(MessageHandler(filters.COMMAND, unknown_commands))
    logger.info("Unknown Command handler added")

    # Handle errors.
    application.add_error_handler(error_handler)

    # Run the bot until the user presses Ctrl-C
    # Pass 'allowed_updates' handle *all* updates including `chat_member` updates
    # To reset this, simply pass `allowed_updates=[]`
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
