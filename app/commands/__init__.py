from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        """Execute the command."""
        pass

class CommandHandler:
    """Registers and executes commands by name."""
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        """Register a command under the given name."""
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """Attempt to execute a registered command using EAFP."""
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")
