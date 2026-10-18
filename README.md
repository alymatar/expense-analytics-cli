# Expense Analytics CLI

A command-line expense tracker built with Python. This project helps users record expenses, calculate spending totals, analyze expenses by category, and save data locally using CSV files.

Built as a learning project to strengthen Python programming fundamentals, file handling, and automated testing.

## Features

- **Add expenses:** Record expense amounts, categories, descriptions, and dates.
- **Input validation:** Reject invalid amounts and empty required text fields.
- **Calculate total spending:** Calculate the total amount of all recorded expenses.
- **Category analytics:** Calculate spending totals for each category.
- **Filter expenses:** Find expenses by category, ignoring capitalization and surrounding spaces.
- **CSV persistence:** Save expenses to a CSV file and load them when the application starts.
- **Automated tests:** Verify calculations, filtering, and CSV persistence using Python's `unittest` framework.

## Technologies

- Python
- CSV file handling
- `pathlib`
- `unittest`
- Git and GitHub

## Requirements

- Python 3.10 or newer recommended
- Git (optional, for cloning the repository)

No external Python packages are required for the core application.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/alymatar/expense-analytics-cli
cd expense-analytics-cli
```

### 2. Run the application

```bash
python main.py
```

Follow the command-line menu to use the application.

### 3. Run the tests

```bash
python -m unittest test_expenses.py
```

## Project Structure

```text
expense-analytics-cli/
├── main.py
├── test_expenses.py
├── README.md
└── .gitignore
```

The application creates or uses a local CSV file to store expenses. That file is intended for local data and should not be committed if it contains personal financial information.

## What I Learned

- Working with Python lists and dictionaries
- Writing reusable functions
- Validating user input with `try` and `except`
- Handling files with `pathlib`
- Reading and writing CSV data
- Testing functions with `unittest`
- Debugging file persistence issues
- Using Git and GitHub for version control

## Future Improvements

- Add expenses by date range
- Export category summaries
- Support editing and deleting expenses
- Migrate from CSV storage to SQLite or PostgreSQL
- Build a REST API using Flask or FastAPI

## Author

Software Engineering | Aspiring Backend Developer

GitHub: https://github.com/alymatar