---
sidebar_label: 'Testing on your Local Machine'
sidebar_position: 6
---

# Testing on your Local Machine

**NOTE**: Following environment variables are used to configure the bot in `PRODUCTION/LOCAL ENVIRONMENT`.

   - `TELEGRAM_TOKEN` -> Telegram bot token.
   - `DEV_CHAT_ID` -> The chat id of the developer where the bot will send debug messages.
   - `GROUP_CHAT_ID` -> The chat id of your group.
   - `SECRET_KEY` -> The secret key for the file decryption process (You can find your key inside `DATA` directory).  

1. You can set these environment variables in your terminal using the following commands:

    ```bash
    export DEV_CHAT_ID=use_your_chat_id_here_obtained_from_idbot
    export TELEGRAM_TOKEN=use_your_telegram_token_obtained_from_botfather_earlier
    export SECRET_KEY=use_your_secret_key_here_obtained_from_encrypting_data
    export GROUP_CHAT_ID=use_your_group_chat_id_here_obtained_from_idbot

    ```
2. Run the bot using the following command:

    On Linux:

    ```bash
    python3 bla_bot.py
    ```
    On Windows:

    ```bash
    py bla_bot.py
    ```
    On Linux using Poetry:

    ```bash
    poetry run python3 bla_bot.py
    ```

    Cool! Now you can start using your bot.  
    Open the Telegram app and search for your bot and start a conversation with it.
    Send `/help` to your bot to see the list of commands. Test all other features and make sure everything is working as expected.

3. Press `Ctrl-C` on the command line to stop the bot.