import os
import pandas as pd

class CSVWriter:
    """
    CSVWriter saves structured entries into a CSV file.
    If the file doesn't exist, it creates it.
    """
    def __init__(self, filepath):
        self.filepath = filepath
        # Create file if not exists
        if not os.path.exists(filepath):
            pd.DataFrame(columns=["Date", "Task", "Hours", "Skills / Learnings"]).to_csv(filepath, index=False)

    def save(self, entries):
        df_existing = pd.read_csv(self.filepath)
        df_new = pd.DataFrame(entries)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        df_combined.to_csv(self.filepath, index=False)
        print(f"Saved {len(entries)} entries to {self.filepath}")
