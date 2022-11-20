# BLA-BOT - A Friendly Telegram Bot

An open-source Telegram Bot written in Python - Tailored for universities/higher education institute groups.

![cover](https://user-images.githubusercontent.com/77499497/189495311-d59a9733-e31b-4fd1-b625-945edaf3f7e6.png)

- [Features](#features)
- [Supported Commands in BOT](#supported-commands-in-bot)
  - [Basic Commands](#basic-commands)
  - [Academic Related Commands](#academic-related-commands)
  - [Other Commands](#other-commands)
- [Basic Requirements](#basic-requirements)
- [Installation](#installation)
  - [Using pip](#using-pip)
  - [Using Poetry](#using-poetry)
- [Usage](#usage)
- [Deploying on Heroku Cloud Platform](#deploying-on-heroku-cloud-platform)
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

## Supported Commands in BOT

### Basic Commands

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

- Heroku Account & Heroku CLI (or suitable platform)
  If you're willing to use Heroku, here they have explained all the steps for getting started with python apps.

  https://devcenter.heroku.com/articles/getting-started-with-python

- Code Editor (such as VS Code)

## Installation

- First clone or download this repository as a Zip file to your local machine.
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

- To properly exit from the virtual environment:

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

- Start bot

  ```bash
  poetry run python3 -m bla_bot.py
  ```

- To properly exit from the shell and the virtual environment:

  ```bash
  exit
  ```

## Usage

1. Make sure to install the dependencies using above steps first and configure the `BOT INFO`, `CHAT/TELEGRAM INFO`, `TIMEZONE DATA` and `UNIVERSITY INFO` in `bla_bot.py`.

   To choose the correct time zone, you can query all the supported time zones like this (run this in a separate terminal):

   ```bash
   python3 -c "import pytz; print(pytz.all_timezones)"
   ```

2. If you're willing to deploy in Heroku Platform, make sure to configure the `HEROKU INFO`.
3. The data files (inside `/DATA` directory) must be filled and formatted as requested, before encrypting.
4. Then run `encrypt_data.py` file (inside `/DATA` directory) to properly encrypt all the data.
5. Following environment variables are used to configure the bot in `PRODUCTION/LOCAL ENVIRONMENT`.

   - `TELEGRAM_TOKEN` -> Telegram bot token.
   - `DEV_CHAT_ID` -> The chat id of the developer where the bot will send debug messages.
   - `GROUP_CHAT_ID` -> The chat id of your group.
   - `SECRET_KEY` -> The secret key for the file decryption process (You can find your key inside `DATA` directory).

- Environment variables for configuring the bot in HEROKU.

  - `PORT` -> The port using for communication.
  - `HEROKU_APP_URL` -> The url of the Heroku app.

- Press `Ctrl-C` on the command line to stop the bot.

## Deploying on Heroku Cloud Platform

**NOTE**:
If you're planning to use Heroku Cloud Platform, under the free plan, the bot will be automatically stopped after some time of inactivity. As a work-around, you can use a service like [Cron-Job.ORG](https://cron-job.org/) (Totally Free) to keep the bot alive in certain times.

> _Heroku Update_  
> Starting November 28th, 2022, free Heroku Dynos, free Heroku Postgres, and free Heroku Data for Redis® will no longer be available.

If you have made any changes to the source code, commit those changes using `git add .` followed by `git commit -m "commit-message"`

If you're willing to use Heroku cloud platform, here's how to do that: (A Heroku account, Heroku CLI and Git will be needed - Read [Basic Requirements](#basic-requirements))

1. Login to Heroku.
   ```bash
   heroku login
   ```
2. Create a heroku app.

   ```bash
   heroku create YOUR-APP-NAME
   ```

3. Next deploy the app:

   ```bash
   git push heroku main
   ```

4. Now set the environment variables (You can also set them on your Heroku dashboard):

   ```bash
    heroku config:set TELEGRAM_TOKEN=YOUR-TELEGRAM-TOKEN
    heroku config:set DEV_CHAT_ID=YOUR-DEV-CHAT-ID
    heroku config:set GROUP_CHAT_ID=YOUR-GROUP-CHAT-ID
    heroku config:set SECRET_KEY=YOUR-SECRET-KEY
    heroku config:set PORT=YOUR-PORT
    heroku config:set HEROKU_APP_URL=YOUR-HEROKU-APP-URL
   ```

## To-Do

- Update Docs
  - Include templates for data files
  - Add more info about data encryption & steps
- New Features
  - User management (Softban/Ban, Mute, Unban, etc.)
  - Add GPA Calculator base code & modules

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

\*\* Heroku, Telegram are copyrights and/or trademarks of their respective owners.

## Disclaimer

The output data of this program is not guaranteed to be correct. Due to unexpected errors in calculations or in other steps, such output data may not be 100% accurate. The author is not responsible for any such faults or any damage caused by this program.
