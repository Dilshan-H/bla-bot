# BLA-BOT - A Friendly Telegram Bot

An open-source Telegram Bot written in Python - Tailored for universities/higher education institute groups.

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License & Copyrights](#license--copyrights)
- [Disclaimer](#disclaimer)

## Features

- Free & Open Source
- Easy to customize & use
-

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

### Using Poetry

- Resolve and install all the dependencies.

  ```bash
  poetry install
  ```

- To start a new shell and activate the virtual environment:

  ```bash
  poetry shell
  ```

- To properly exit from the shell and the virtual environment:

  ```bash
  exit
  ```

## Usage

- Make sure to install the dependencies using above steps first and configure the `BOT INFO`, `CHAT/TELEGRAM INFO`, `TIMEZONE DATA` and `UNIVERSITY INFO` in `bla_bot.py`.
- If you're willing to deploy in Heroku Platform, make sure to configure the `HEROKU INFO`.
- The data files (inside `/DATA` directory) must be filled and formatted as requested before encryption.
- Then run `encrypt_data.py` file (inside `/DATA` directory) to properly encrypt all the data.
- Following environment variables are used to configure the bot in `PRODUCTION ENVIRONMENT`.

  - `TELEGRAM_TOKEN` -> Telegram bot token.
  - `DEV_CHAT_ID` -> The chat id of the developer where the bot will send debug messages.
  - `GROUP_CHAT_ID` -> The chat id of your group.
  - `SECRET_KEY` -> The secret key for the file decryption process (You can find your key inside `DATA` directory).

- Environment variables for configuring the bot in HEROKU.

  - `PORT` -> The port using for communication.
  - `HEROKU_APP_URL` -> The url of the Heroku app.

- Press `Ctrl-C` on the command line to stop the bot.

## Deploying on Heroku Cloud Platform

**NOTE**:

> _Heroku Update_  
> Starting November 28th, 2022, free Heroku Dynos, free Heroku Postgres, and free Heroku Data for Redis® will no longer be available.

To choose the correct time zone, you can query all the supported time zones like this;

```python
import pytz
pytz.all_timezones
```

If you have made any changes (such as changing the Timezone in routes.py) to the source code, commit those changes using `git add .` and `git commit -m "commit-message"`

If you're willing to use Heroku cloud platform, here's how to do that: (A Heroku account, Heroku CLI and Git will be needed. (Read [Basic Requirements](#basic-requirements))

## Credits

### Python-Telegram-Bot

> This library provides a pure Python, asynchronous interface for the Telegram Bot API. It's compatible with Python versions 3.7+.

- https://python-telegram-bot.org/
- https://github.com/python-telegram-bot/python-telegram-bot

python-telegram-bot is distributed under a [LGPLv3 license](https://www.gnu.org/licenses/lgpl-3.0.html).

## Contributing

Got an idea? Found a bug? Feel free to [open an issue](https://github.com/Dilshan-H/bla-bot/issues/new) or submit a pull request.

## License & Copyrights

**The MIT License**

This program is free software: you can redistribute it and/or modify it under the terms of the **MIT License**

\*\*Heroku, Telegram are copyrights and/or trademarks of their respective owners.

## Disclaimer

The output data of this program is not guaranteed to be correct. Due to unexpected errors in calculations or in other steps, such output data may not be 100% accurate. The author is not responsible for any such faults or any damage caused by this program.
