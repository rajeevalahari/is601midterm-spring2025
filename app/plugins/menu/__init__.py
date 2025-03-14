import logging
from app.commands import Command

class MenuCommand(Command):
    def execute(self):
        logging.info("MenuCommand: Displaying available commands")
        print("Available commands:")
        print("  add   -> Adds two numbers")
        print("  sub   -> Subtracts two numbers")
        print("  mul   -> Multiplies two numbers")
        print("  div   -> Divides two numbers")
        print("  exit  -> Exits the application")
        print("  menu  -> Displays this menu")
