import unittest
import tempfile
from pathlib import Path
from main import (
    calculate_total, 
    filter_expenses_by_category, 
    save_expenses, 
    load_expenses
    )

class TestExpensesCalculations(unittest.TestCase):
    def test_calculate_total(self):
        expenses = [
            {"amount": 100.0, "category": "Food", "description": "Groceries", "date": "2023-01-01"},
            {"amount": 50.0, "category": "Transport", "description": "Bus fare", "date": "2023-01-02"},
            {"amount": 25.0, "category": "Food", "description": "burger", "date": "2023-01-03"}
        ]
        result = calculate_total(expenses)
        expected_total = 175.0

        self.assertEqual(result, expected_total)

    def test_calculate_total_empty(self):
        expenses = []
        result = calculate_total(expenses)
        self.assertEqual(result, 0.0)

    def test_calculate_total_negative_amounts(self):
        expenses = [
            {"amount": -100.0, "category": "Food", "description": "Groceries", "date": "2023-01-01"},
            {"amount": 50.0, "category": "Transport", "description": "Bus fare", "date": "2023-01-02"}
        ]
        result = calculate_total(expenses)
        expected_total = -50.0

        self.assertEqual(result, expected_total)

    def test_calculate_total_large_numbers(self):

        expenses = [
            {"amount": 10000, "category": "Investment", "description": "Stocks", "date": "2023-01-01"},
            {"amount": 20000, "category": "Investment", "description": "Bonds", "date": "2023-01-02"}
        ]
        result = calculate_total(expenses)
        expected_total = 30000

        self.assertEqual(result, expected_total)

    def test_calculate_total_one_expense(self):
        expenses = [
            {"amount": 100.0, "category": "Food", "description": "Groceries", "date": "2023-01-01"}
        ]
        result = calculate_total(expenses)
        expected_total = 100.0

        self.assertEqual(result, expected_total)

    def test_filter_expenses_by_category(self):
        expenses = [
            {"amount": 100.0, "category": "Food", "description": "Groceries", "date": "2023-01-01"},
            {"amount": 50.0, "category": "Transport", "description": "Bus fare", "date": "2023-01-02"},
            {"amount": 25.0, "category": "Food", "description": "burger", "date": "2023-01-03"}
        ]
        result = filter_expenses_by_category(expenses, "Food")
        expected_result = [
            {"amount": 100.0, "category": "Food", "description": "Groceries", "date": "2023-01-01"},
            {"amount": 25.0, "category": "Food", "description": "burger", "date": "2023-01-03"}
        ]

        self.assertEqual(result, expected_result)

    def test_filter_category_ignores_case_and_spaces(self):
        expenses = [
                   {"amount": 100.0, "category": "Food", "description": "Groceries", "date": "2023-01-01"},
                   {"amount": 50.0, "category": "Transport", "description": "Bus fare", "date": "2023-01-02"},
                   {"amount": 25.0, "category": "food", "description": "burger", "date": "2023-01-03"}
               ]
        result = filter_expenses_by_category(expenses, " food ")
        expected_result = [
            {"amount": 100.0, "category": "Food", "description": "Groceries", "date": "2023-01-01"},
            {"amount": 25.0, "category": "food", "description": "burger", "date": "2023-01-03"}
        ]
        self.assertEqual(result, expected_result)

    def test_filter_expenses_by_category_not_found(self):
        expenses = [
                    {"amount": 100.0, "category": "Food", "description": "Groceries", "date": "2023-01-01"},
                    {"amount": 50.0, "category": "Transport", "description": "Bus fare", "date": "2023-01-02"},
                    {"amount": 25.0, "category": "Food", "description": "burger", "date": "2023-01-03"}
                ]

        result = filter_expenses_by_category(expenses, "Games")

        self.assertEqual(result, [])


    def test_save_and_load_expenses(self):
        expenses = [
            {
                "amount": 100.0,
                "category": "Food",
                "description": "Groceries",
                "date": "2026-10-18"
            },
            {
                "amount": 50.0,
                "category": "Transport",
                "description": "Bus fare",
                "date": "2026-10-18"
            }
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "expenses.csv"

            save_expenses(expenses, file_path)
            loaded_expenses = load_expenses(file_path)

            self.assertEqual(loaded_expenses, expenses)

    def test_load_expenses_when_file_does_not_exist(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "missing.csv"

            result = load_expenses(file_path)

            self.assertEqual(result, [])

    def test_save_expenses_appends_to_same_file(self):
        expense1 = [
                    {
                        "amount": 100.0,
                        "category": "Food",
                        "description": "Groceries",
                        "date": "2026-10-18"
                    }
                ]
        expense2 = [
                    {
                        "amount": 50.0,
                        "category": "Transport",
                        "description": "Bus fare",
                        "date": "2026-10-18"
                    }
                ]
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "expenses.csv"
            save_expenses(expense1, file_path)
            save_expenses(expense2, file_path)

            result = load_expenses(file_path)
            expenses= expense1 + expense2
            self.assertEqual(result, expenses)

if __name__ == '__main__':
    unittest.main()