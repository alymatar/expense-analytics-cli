# Expense Analytics CLI

A command-line expense tracker in Python. Record expenses, see the total and per-category spending, filter by category, and keep everything in a local CSV file between runs.

It uses only the Python standard library and has 11 `unittest` tests.

## Features

- **Add expenses:** amount, category and description, with today's date filled in automatically. You can add several in one go.
- **Input validation:** amounts must be numbers greater than zero, and text fields can't be empty.
- **Spending report:** the total of all expenses, plus a total for each category.
- **Filter by category:** matching ignores capitalisation and surrounding spaces, and the filtered view shows its own total.
- **CSV persistence:** expenses are saved to `expenses.csv` and loaded again when the app starts. The file is created automatically and is git-ignored.
- **Tests:** totals (including empty, negative and large values), filtering, and saving/loading the CSV file.

## Tech stack

Python 3 (standard library only): `csv`, `pathlib`, `datetime`, `unittest`.

## Example

```text
1. Add an expense
2. View all expenses
3. View the spending report
4. Filter expenses by category
5. Exit
please select an option (1-5): 3
========= EXPENSE REPORT ==========
Total expenses:  195.50
Spending by category:
Food:  150.00
Transport:  45.50
===================================
```

## Run locally

Requires Python 3.10 or newer. Nothing to install.

```bash
git clone https://github.com/alymatar/expense-analytics-cli.git
cd expense-analytics-cli
python main.py
```

## Run the tests

```bash
python -m unittest test_expenses.py
```

## Project structure

```text
expense-analytics-cli/
├── main.py            # menu, input validation, calculations, CSV load/save
├── test_expenses.py   # unittest suite (11 tests)
├── README.md
└── .gitignore         # ignores expenses.csv, caches and virtualenvs
```

## What I learned

- Structuring a program as small, testable functions
- Validating user input with `try`/`except`
- Reading and writing CSV files with `csv.DictReader`/`DictWriter` and `pathlib`
- Writing unit tests, including tests that use temporary files

## Next steps

- Edit and delete expenses, and filter by date range
- Move storage from CSV to SQLite or PostgreSQL
- Expose the same logic as a REST API with FastAPI
