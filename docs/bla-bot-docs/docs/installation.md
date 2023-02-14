---
sidebar_label: 'Installation'
sidebar_position: 3
---

# Installation

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

:::tip QUICK TIP

Whenever you need to properly exit from the virtual environment, just run the following command:

  ```bash
  deactivate
  ```

:::

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

:::tip QUICK TIP

Whenever you need to properly exit from the shell and the virtual environment run the following command :

  ```bash
  exit
  ```

:::