import pandas as pd

class SummaryAgent:
    """
    Summary Agent generates a weekly summary from CSV.
    """
    def generate(self, csv_file):
        df = pd.read_csv(csv_file)
        print("\n===== Weekly Summary =====")
        print(df)
