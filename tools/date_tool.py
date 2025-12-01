from datetime import datetime

class DateTool:
    """
    Simple date tool to get current date.
    """
    def today(self):
        return datetime.today().strftime("%Y-%m-%d")
