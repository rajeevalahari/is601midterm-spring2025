import os
import logging
from app.commands import Command
from app.plugins.history_facade import HistoryFacade

class ShowHistoryCommand(Command):
    """
    Show the last 5 calculations from the CSV (if any).
    """

    def execute(self):
        csv_file = os.getenv("CALC_HISTORY_FILE", "calc_history.csv")
        facade = HistoryFacade(csv_file)

        df = facade.load_history()
        if df.empty:
            print("No history yet.")
        else:
            # Display only the last 5 rows
            last_five = df.tail(5)
            print("\nLast 5 Calculations:\n", last_five, "\n")

        logging.info("ShowHistoryCommand: displayed last 5 calculations.")
