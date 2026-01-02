# CLI Todo Application

A simple, command-line interface (CLI) todo application built in Python.

## Setup

No special setup is required. The application runs using Python 3.13+ and does not have any external dependencies.

## Usage

All commands are run through the `src/cli.py` script.

### Add a Task

```bash
python -m todo add --title "My First Task" --description "This is a description for my task."
```

### List All Tasks

```bash
python -m todo list
```

### Update a Task

```bash
python -m todo update 1 --title "New Title" --description "New Description"
```

### Mark a Task as Complete

```bash
python -m todo complete 1
```

### Mark a Task as Incomplete

```bash
python -m todo incomplete 1
```

### Delete a Task

```bash
python -m todo delete 1
```# -Todo-In-Memory-Python-Console-App
