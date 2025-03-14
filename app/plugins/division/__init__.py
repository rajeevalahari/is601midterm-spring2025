import logging
from app.commands import Command

class DivideCommand(Command):
    def execute(self):
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if b == 0:
                logging.error("DivideCommand: Division by zero attempted")
                print("Error: Division by zero is not allowed.")
                return
            result = a / b
            logging.info("DivideCommand: %s / %s = %s", a, b, result)
            print(f"Result: {result}")
        except ValueError:
            logging.error("DivideCommand: Invalid input encountered")
            print("Invalid input. Please enter numeric values.")
