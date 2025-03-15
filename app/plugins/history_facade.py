import os
import pandas as pd

class HistoryFacade:
    """A facade to abstract loading/appending operations from/to a CSV file."""
    def __init__(self, csv_file="calc_history.csv"):
        self.csv_file = csv_file

    def load_history(self):
        """Load history from CSV if it exists; otherwise, return an empty DataFrame."""
        if os.path.exists(self.csv_file):
            return pd.read_csv(self.csv_file)
        return pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])

    def save_history(self, df):
        """Save the given DataFrame to CSV, overwriting the file."""
        df.to_csv(self.csv_file, index=False)

    def clear_history(self):
        """Remove the CSV file if it exists."""
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)
    
    def append_operation(self, operation, operand1, operand2, result):
        """Appends a single operation row to the CSV."""
        df = self.load_history()

        new_row = {
            "operation": operation,
            "operand1": operand1,
            "operand2": operand2,
            "result": result
        }

        # Instead of df.append(...):
        new_df = pd.DataFrame([new_row])
        df = pd.concat([df, new_df], ignore_index=True)

        self.save_history(df)
