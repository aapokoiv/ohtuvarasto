# ohtuvarasto

[![GHA workflow badge](https://github.com/aapokoiv/ohtuvarasto/actions/workflows/main.yml/badge.svg)](https://github.com/aapokoiv/ohtuvarasto/actions/workflows/main.yml)
[![codecov](https://codecov.io/github/aapokoiv/ohtuvarasto/graph/badge.svg?token=0KPP2EA4B6)](https://codecov.io/github/aapokoiv/ohtuvarasto)

## Warehouse Management System

A simple warehouse management system with a web interface built with Flask.

### Features

- Create multiple warehouses with custom capacity and initial stock
- View all warehouses in a list
- Add items to warehouses
- Remove items from warehouses
- Track available space in each warehouse

### Installation

Install dependencies using Poetry:

```bash
poetry install
```

### Running the Application

Start the Flask web server:

```bash
cd src
FLASK_APP=app.py poetry run python -m flask run
```

Then open your browser and navigate to `http://localhost:5000`

### Running Tests

Run unit tests:

```bash
poetry run pytest
```

Run tests with coverage:

```bash
poetry run coverage run --branch -m pytest
poetry run coverage report
```

Run pylint:

```bash
poetry run pylint src
```

### Robot Framework Tests

The project includes Robot Framework tests for the web interface. To run them:

1. Start the Flask application in one terminal:
```bash
cd src
FLASK_APP=app.py poetry run python -m flask run
```

2. In another terminal, run the Robot tests:
```bash
poetry run robot src/tests/robot/
```

Note: Robot tests require Chrome/Chromium browser and chromedriver to be installed.
