import os
import logging
from app.commands import Command
from app.plugins.history_facade import HistoryFacade

class ClearHistoryCommand(Command):
    """
    Clear the CSV history (delete the file).
    """

    def execute(self):
        csv_file = os.getenv("CALC_HISTORY_FILE", "calc_history.csv")
        facade = HistoryFacade(csv_file)

        facade.clear_history()
        print("History cleared.")
        logging.info("ClearHistoryCommand: history file cleared.")
