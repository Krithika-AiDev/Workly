class ExtractionAgent:
    """
    Extraction Agent parses raw text and extracts structured information.
    Here, we do a simple static mapping for demonstration.
    """
    def extract(self, text_input):
        return [{
            "Date": "2025-12-01",
            "Task": "Automated ticket creation, Fixed bugs, Learned async Python",
            "Hours": 4,
            "Skills / Learnings": "Workflow automation, Debugging, Async programming"
        }]
