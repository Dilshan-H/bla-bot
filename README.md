# BLA-BOT - A Friendly Telegram Bot

An open-source Telegram Bot written in Python - Tailored for universities/higher education institute groups.

🔴 This is `v1 branch` - Ready to be deployed on **Render** platform. Due to certain restrictions, we have to move away from it. This branch will **not** be updated in future! Please consider using `master` branch instead.

<!-- Shield Badges -->

![GitHub license](https://img.shields.io/github/license/Dilshan-H/bla-bot?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/Dilshan-H/bla-bot?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/Dilshan-H/bla-bot?style=for-the-badge)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Dilshan-H/bla-bot?style=for-the-badge)

![GitHub stars](https://img.shields.io/github/stars/Dilshan-H/bla-bot?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/Dilshan-H/bla-bot?style=for-the-badge)

![cover](https://user-images.githubusercontent.com/77499497/189495311-d59a9733-e31b-4fd1-b625-945edaf3f7e6.png)

- [Features](#features)
- [Screenshots](#screenshots)
- [Supported Commands in BOT](#supported-commands-in-bot)
  - [Basic Commands](#basic-commands)
  - [Academic Related Commands](#academic-related-commands)
  - [Other Commands](#other-commands)
- [Basic Requirements](#basic-requirements)
- [Installation](#installation)
  - [Using pip](#using-pip)
  - [Using Poetry](#using-poetry)
- [Usage](#usage)
  - [Testing on your Local Machine](#testing-on-your-local-machine)
  - [Deploying on Render](#deploying-on-render)
    - [Deploy Using Blueprint](#deploy-using-blueprint)
    - [Deploy Manually](#deploy-manually)
    - [Final Steps](#final-steps)
  - [Deploying on Heroku Cloud Platform [Deprecated]](#deploying-on-heroku-cloud-platform-deprecated)
- [To-Do](#to-do)
- [Contributing](#contributing)
- [Credits](#credits)
- [License & Copyrights](#license--copyrights)
- [Disclaimer](#disclaimer)

## Features

- Free & Open Source
- Easy to customize & use
- Support for data encryption
- Enhanced performance with caching
- Intelligent search & indexing
- Logging enabled
- Secure & Private

## Screenshots

| ![ Telegram_Bot_Image_1 ](https://github.com/Dilshan-H/bla-bot/assets/77499497/e3a80a75-c833-4b0f-a269-cff7c931b8e7) | ![ Telegram_Bot_Image_2 ](https://github.com/Dilshan-H/bla-bot/assets/77499497/5cbe13c6-08e9-4ffa-821f-2774a02430b4) |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| ![ Telegram_Bot_Image_3 ](https://github.com/Dilshan-H/bla-bot/assets/77499497/e9085a69-447e-467e-adfd-b67e82de6894) | ![ Telegram_Bot_Image_4 ](https://github.com/Dilshan-H/bla-bot/assets/77499497/aefa3956-e578-481b-acd0-f4ce53a44242) |

## Why use **BLA-BOT** in your academic group?

- **Easy to use**: The bot is easy to use and understand. You can add BLA-BOT to your academic group and easily provide information to your fellow students.
- **Cool features**: BLA-BOT has some cool features like GPA info, birthday wishes, announce to your group as bot, additional academic resources and much more.
- **Easy to customize**: The bot is easy to customize and modify according to your needs.
- **Secure**: The bot is secure and private. Users only see the data they are authorized to see. Even though any other 3rd party can add your bot to their group, they won't be able to utilize some of the bot's features. (like results, student info, etc.) Some of the features are only available to the group admins.
  Additionally, if any unauthorized person tries to access the bot's data, they won't be able to do so. The data is encrypted and only the bot can decrypt it.
- **Unauthorized access alert**: The bot will alert the group admins about the unauthorized access attempts via dm (This only works if you have already interacted with your bot via dm previously).
- **Documentation**: The bot is well documented and has a detailed README file. You can easily understand how the bot works and how to customize it according to your needs.

## Supported Commands in BOT

### General Commands

- `/start` or `/help` - See all the commands
- `/whois` - Get info about someone
- `/about` - Read about the bot
- `/cancel` - Cancel any running operation

### Academic Related Commands

- `/gpa` - Show your gpa & results
- `/staff` - Get staff info
- `/{UNI_NAME_SHORT}` - Read about institute
- `/resources` - Explore academic/other resources

### Other Commands

- `/tasks` - Manage scheduled tasks (Admin only)
- `/announce` - Broadcast a message (Admin only)

## Basic Requirements

- Python3 and Pip

- Git

  https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
  https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup

- Render Account (either free or paid) - https://render.com/

  -- OR --

  Your preferred cloud platform (such as Heroku) - Ex:
  Heroku Account & Heroku CLI if you're willing to use Heroku, [Here](https://devcenter.heroku.com/articles/getting-started-with-python) they have explained all the steps for getting started with python apps.

- Code Editor (such as VS Code)
- GitHub/GitLab Account for deploying the bot with Render

## Installation

- First fork this repository and clone it to your local machine.
- Navigate to the directory.

  ```bash
  cd bla-bot
  ```

### Using pip

- Create a virtual environment.

  ```bash
  python3 -m venv virtualenv
  ```

- Activate virtual environment.

  **Linux**:

  ```bash
  source virtualenv/bin/activate
  ```

  **Windows**:

  ```bash
  virtualenv\Scripts\activate
  ```

- Install dependencies.

  ```bash
  pip install -r requirements.txt
  ```

  Now go ahead and configure your bot according to your needs. (See [Usage](#usage))

- Whenever you need to properly exit from the virtual environment, just run the following command:

  ```bash
  deactivate
  ```

### Using Poetry

- Resolve and install all the dependencies.

  ```bash
  poetry install
  ```

- To start a new shell and activate the virtual environment:

  ```bash
  poetry shell
  ```

  Now go ahead and configure your bot according to your needs. (See [Usage](#usage))

- Whenever you need to properly exit from the shell and the virtual environment run the following command :

  ```bash
  exit
  ```

## Usage

1. Make sure to install the dependencies using above steps first.

2. Configure the `BOT INFO`, `TIMEZONE DATA` and `UNIVERSITY INFO` in `bla_bot.py`.

   - To choose the correct time zone for `TIME_ZONE`, you can query all the supported time zones like this (run this in a separate terminal):

     ```bash
     python3 -c "import pytz; print(pytz.all_timezones)"
     ```

     Type the name of the time zone you want to use in `TIME_ZONE` variable.

   - Replace university name, short name, and other info in `UNIVERSITY_INFO` section.

3. The data files (inside `/DATA` directory) must be filled and formatted as requested, before encrypting. Then run `encrypt_data.py` file (inside `/DATA` directory) to properly encrypt all the data. ([Read More](/DATA/README.md#data-formatting--encrypting))
4. Obtain a telegram bot token from [BotFather](https://t.me/BotFather) (This will be needed as we proceed further.). Start a conversation with BotFather on Telegram and follow the instructions to create a new bot. You will receive a token that you can use to authorize your bot and send requests to the Bot API.
5. Obtain your personal chat id (This is what we call `DEV_CHAT_ID`) and group chat id (This is what we call `GROUP_CHAT_ID`, id of the group that you're going to add the bot) using [IDBot](https://t.me/myidbot) (These ids will be needed as we proceed further.). Start a conversation with IDBot on Telegram and follow the instructions to get your chat ids.

## Testing on your Local Machine

**NOTE**: Following environment variables are used to configure the bot in `LOCAL ENVIRONMENT`.

- `TELEGRAM_TOKEN` -> Telegram bot token.
- `DEV_CHAT_ID` -> The chat id of the developer where the bot will send debug messages.
- `GROUP_CHAT_ID` -> The chat id of your group.
- `SECRET_KEY` -> The secret key for the file decryption process (You can find your key inside `DATA` directory).

1. Create a `.env` file in the root directory of the project and add the following environment variables to it:

```bash
DEV_CHAT_ID=use_your_chat_id_here_obtained_from_idbot
ENV=dev # Use 'prod' for production environment
GROUP_CHAT_ID=use_your_group_chat_id_here_obtained_from_idbot
PORT=8443
RENDER_APP_URL=use_your_render_app_url_here_obtained_from_render_dashboard # Keep this empty if you're running the bot locally
SECRET_KEY=use_your_secret_key_here_obtained_from_encrypting_data
TELEGRAM_TOKEN=use_your_telegram_token_obtained_from_botfather_earlier
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

## Deploying on Render

[Render](https://render.com/) is a cloud platform that allows you to deploy your apps in a few clicks. It's free for small projects and has a generous free tier.

**NOTE**:
If you're planning to use Render Cloud Platform, under the free plan, the bot will be automatically stopped after some time of inactivity (~15 minutes). As a work-around, you can use a service like [Cron-Job.ORG](https://cron-job.org/) (Totally Free) to keep the bot alive in certain times.

If you have made any changes to the source code, commit those changes using `git add .` followed by `git commit -m "your-commit-message"` and then push those changes to your REMOTE branch on either GitHub or GitLab (This is a mandatory requirement).

- ### Deploy Using Blueprint

  If you have already pushed your changes (your data files) to the remote repository; now you can deploy your bot on Render in just a few clicks.
  We have provided a render app [blueprint specification](https://render.com/docs/blueprint-spec) which makes the deployment process much easier. Just click on the button below and sign into your Render account.

  [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

  You will have to provide the necessary values for the environment variables at first (You can refer the following table for details about the environment variables), except for `RENDER_APP_URL`.
  Make sure to update that later. You can find environment variables section in the `Environment` tab of your web service for updating that.

- ### Deploy Manually

  1. Login to your [Render account](https://dashboard.render.com/).
  2. Click on `New Service` and select **web service**.
  3. Now you can connect your GitHub or GitLab repository to Render.

  After this process, you have to configure the environment variables as mentioned above. You can find environment variables section in the `Environment` tab of your web service.

  Add these keys and respective values to the environment variables:

| Key            | Value                                                                                                                                                                        |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DEV_CHAT_ID    | Your chat id obtained from _idbot_                                                                                                                                           |
| ENV            | `prod`                                                                                                                                                                       |
| GROUP_CHAT_ID  | Your group chat id obtained from _idbot_                                                                                                                                     |
| RENDER_APP_URL | The url of the Render app. (Ex: `https://your-bot-name.onrender.com`) - Can obtain from [Render Dashboard](<[https://dashboard.render.com/](https://dashboard.render.com/)>) |
| PORT           | `8443`                                                                                                                                                                       |
| SECRET_KEY     | Your secret key here obtained after data encryption procedure                                                                                                                |
| TELEGRAM_TOKEN | Your Telegram token obtained from _botfather_ earlier                                                                                                                        |

Now click on `Save Changes` and your bot will be deployed on Render.

### Final Steps

Now open your web browser and visit the following URL - Make sure to replace the string `{YOUR-BOT-TOKEN}` with your bot's token and the `{RENDER-URL}` with your web service URL.

https://api.telegram.org/bot{YOUR-BOT-TOKEN}/setWebhook?url={RENDER-URL}

You can verify webhook information using following URL:  
 https://api.telegram.org/bot{YOUR-BOT-TOKEN}/getWebhookInfo

If everything goes well, you can start using your bot right away. Open the Telegram app and search for your bot and start a conversation with it. Send `/help` to your bot to see the list of commands. Test all other features and make sure everything is working as expected.

Then add your bot to your group and start using it.

**NOTE**:  
You can use [BotFather](https://t.me/botfather) to change the bot's name and profile picture. Also do not forget to add all the commands to your bot using BotFather (Edit Commands). So, users can easily browse all the commands.

## Deploying on Heroku Cloud Platform [Deprecated]

> _Heroku Update_  
> Starting November 28th, 2022, free Heroku Dynos, free Heroku Postgres, and free Heroku Data for Redis® will no longer be available.

<details>
  <summary>Steps to configure on Heroku</summary>

**NOTE**:
If you're planning to use Heroku Cloud Platform, under the free plan, the bot will be automatically stopped after some time of inactivity. As a work-around, you can use a service like [Cron-Job.ORG](https://cron-job.org/) (Totally Free) to keep the bot alive in certain times.

If you have made any changes to the source code, commit those changes using `git add .` followed by `git commit -m "commit-message"`

If you're willing to use Heroku cloud platform, here's how to do that: (A Heroku account, Heroku CLI and Git will be needed - Read [Basic Requirements](#basic-requirements))

1.  Login to Heroku.
    ```bash
    heroku login
    ```
2.  Create a heroku app.

    ```bash
    heroku create YOUR-APP-NAME
    ```

3.  Next deploy the app:

    ```bash
    git push heroku main
    ```

4.  Now set the environment variables (You can also set them on your Heroku dashboard):

          ```bash
            heroku config:set TELEGRAM_TOKEN=YOUR-TELEGRAM-TOKEN
            heroku config:set DEV_CHAT_ID=YOUR-DEV-CHAT-ID
            heroku config:set GROUP_CHAT_ID=YOUR-GROUP-CHAT-ID
            heroku config:set SECRET_KEY=YOUR-SECRET-KEY
            heroku config:set PORT=8443
            heroku config:set HEROKU_APP_URL=YOUR-HEROKU-APP-URL
            heroku config:set ENV=prod
          ```

    </details>

## To-Do

- New Features
  - User management (Softban/Ban, Mute, Unban, etc.)
  - Add/Link GPA Calculator base code & modules

## Contributing

Got an idea? Found a bug? Feel free to [open an issue](https://github.com/Dilshan-H/bla-bot/issues/new) or submit a pull request.

Fork the repository, make your changes and submit a pull request. It's that much easy! If you're not sure how to do that, here's a [guide](https://opensource.com/article/19/7/create-pull-request-github).

## Credits

### Python-Telegram-Bot

> This library provides a pure Python, asynchronous interface for the Telegram Bot API. It's compatible with Python versions 3.7+.

- https://python-telegram-bot.org/
- https://github.com/python-telegram-bot/python-telegram-bot

python-telegram-bot is distributed under a [LGPLv3 license](https://www.gnu.org/licenses/lgpl-3.0.html).

## License & Copyrights

**The MIT License**

This program is free software: you can redistribute it and/or modify it under the terms of the **MIT License**

\*\* Render, Heroku, Telegram, VS Code are copyrights and/or trademarks of their respective owners.

## Disclaimer

The output data of this program is not guaranteed to be correct. Due to unexpected errors in calculations or in other steps, such output data may not be 100% accurate. The author is not responsible for any such faults or any damage caused by this program.
