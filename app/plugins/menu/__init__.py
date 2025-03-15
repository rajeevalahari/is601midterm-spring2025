import logging
from app.commands import Command

class MenuCommand(Command):
    def execute(self):
        logging.info("MenuCommand: Displaying available commands")
        print("Available commands:")
        print("  addition   -> Adds two numbers")
        print("  subtraction   -> Subtracts two numbers")
        print("  multplication   -> Multiplies two numbers")
        print("  division   -> Divides two numbers")
        print("  exit  -> Exits the application")
        print("  menu  -> Displays this menu")
        print("  showhistory  -> Shows history(last 5 calculations)")
        print("  clearhistory  -> Clears history")

