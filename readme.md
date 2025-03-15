# Advanced Python Calculator

## Project Overview

This project implements an advanced command-line calculator emphasizing professional software engineering practices, including modular architecture, robust logging, dynamic configuration via environment variables, advanced data management using Pandas, and comprehensive testing using Pytest.

---

## Core Features

### Command-Line Interface (REPL)

A user-friendly Read-Eval-Print Loop (REPL) for:

- Arithmetic operations: Addition, Subtraction, Multiplication, Division.
- History commands: `showhistory`, `clearhistory`.
- Dynamic plugin commands listed via `menu`.

## Plugin System

Plugins dynamically load commands at runtime, allowing easy integration without altering core code. Implemented commands include:

- Arithmetic (`addition`, `subtraction`, `multiplication`, `division`)
- History management (`showhistory`, `clearhistory`)

## History Management

Calculation history is efficiently managed with Pandas, storing records in CSV format (`history.csv`).

- Commands:
  - `showhistory`: Displays the last five calculations.
  - `clearhistory`: Clears the entire calculation history.

[History Management Code](app/plugins/history_facade.py)

---

## Design Patterns

Implemented design patterns include:

- **Facade Pattern:** Simplifies interactions with Pandas history operations. [Facade Implementation](app/plugins/history_facade.py)
- **Command Pattern:** Encapsulates calculator and history functionalities as REPL commands. [Commands Implementation](app/commands)
- **Factory Method, Singleton, Strategy Patterns:** Structured within the application's command and plugin management.

---

## Environment Variables

Dynamic configuration handled via environment variables:

- `ENVIRONMENT`: Switches between `DEVELOPMENT`, `TESTING`, and `PRODUCTION` modes.
- `CALC_HISTORY_FILE`: Defines the file path for the calculation history CSV.
- `LOG_LEVEL`: HELPS IN LOGGING IDENTIFICATION `INFO`.

[Environment Variables Usage](app/__init__.py)

---

## Logging Practices

Professional logging integrated with Python's `logging` library:

- Logs operational messages, errors, warnings, and debug information.
- Configurable via environment variables (`LOG_LEVEL`) and external `logging.conf` file.

[Logging Implementation](app/__init__.py)

---

## Error Handling (LBYL vs. EAFP)

Used `try-except` blocks to demonstrate:

- **EAFP**: Managing exceptions during user input parsing.
- **LBYL**: Checking conditions before accessing files or performing operations.

[Error Handling Example](app/plugins/addition/__init__.py)

---


Run tests using:
```bash
pytest
pytest --cov
pytest --pylint
pytest --pylint --cov
```

---

## GitHub Actions

Continuous Integration setup via GitHub Actions:

- Tests and lint checks automatically run on every push.
- Ensures passing test coverage before merges.

[GitHub Actions Workflow](.github/workflows/python-ci.yml)

---

## Installation and Usage

### Requirements

Install required dependencies:

```bash
pip install -r requirements.txt
```

### Run Application

Start the REPL by running:

```bash
python main.py
```

Type `menu` for a list of available commands, or type `exit` to quit.

---


## Video Demonstration

[https://youtu.be/e9rTya5htvA](#)

