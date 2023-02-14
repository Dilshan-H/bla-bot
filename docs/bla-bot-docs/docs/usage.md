---
sidebar_label: 'Usage'
sidebar_position: 4
---

# Usage

1. Make sure to install the dependencies using above steps first.

2. Configure the `BOT INFO`, `TIMEZONE DATA` and `UNIVERSITY INFO` in `bla_bot.py`.
    - To choose the correct time zone for `TIME_ZONE`, you can query all the supported time zones like this (run this in a separate terminal):

      ```bash
      python3 -c "import pytz; print(pytz.all_timezones)"
      ```
      Type the name of the time zone you want to use in `TIME_ZONE` variable.
    - Replace university name, short name, and other info in `UNIVERSITY_INFO` section.

3. The data files (inside `/DATA` directory) must be filled and formatted as requested, before encrypting. Then run `encrypt_data.py` file (inside `/DATA` directory) to properly encrypt all the data. ([Read More](/docs/data-formatting-encrypting))
4. Obtain a telegram bot token from [BotFather](https://t.me/BotFather) (This will be needed as we proceed further.). Start a conversation with BotFather on Telegram and follow the instructions to create a new bot. You will receive a token that you can use to authorize your bot and send requests to the Bot API.
5. Obtain your personal chat id (This is what we call `DEV_CHAT_ID`) and group chat id (This is what we call `GROUP_CHAT_ID`, id of the group that you're going to add the bot) using [IDBot](https://t.me/myidbot) (These ids will be needed as we proceed further.). Start a conversation with IDBot on Telegram and follow the instructions to get your chat ids.

:::danger WARNING

Do not share your `TELEGRAM_TOKEN` and `SECRET_KEY` with anyone. These are sensitive information and should be kept secret!

:::