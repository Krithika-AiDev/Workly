from agents.collector_agent import CollectorAgent
from agents.extraction_agent import ExtractionAgent
from agents.summary_agent import SummaryAgent
from tools.csv_writer import CSVWriter

# Initialize agents and tools
collector = CollectorAgent()
extractor = ExtractionAgent()
summary = SummaryAgent()
csv_writer = CSVWriter("data/work_log.csv")

# Sample daily input
daily_input = collector.collect(
    "Today I worked on automating tickets, fixed bugs, and learned async Python."
)

# Extract structured info
tasks = extractor.extract(daily_input)

# Save to CSV
csv_writer.save(tasks)

# Generate weekly summary (minimal)
summary.generate("data/work_log.csv")
