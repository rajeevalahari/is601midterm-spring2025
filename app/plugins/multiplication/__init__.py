import os
import logging
from app.commands import Command
from app.plugins.history_facade import HistoryFacade

class MultiplyCommand(Command):
    def execute(self):
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = a * b
            logging.info("MultiplyCommand: %s * %s = %s", a, b, result)
            print(f"Result: {result}")
            csv_file = os.getenv("CALC_HISTORY_FILE", "calc_history.csv")
            facade = HistoryFacade(csv_file)
            facade.append_operation("multplication", a, b, result)
        except ValueError:
            logging.error("MultiplyCommand: Invalid input encountered")
            print("Invalid input. Please enter numeric values.")
