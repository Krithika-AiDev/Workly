### Problem Statement

In today’s hybrid and remote work environments, keeping track of daily tasks, learnings, and personal skill growth is often inconsistent. Most people jot notes across scattered platforms—Notepad, or Excel—and rarely revisit them systematically. This makes it difficult to reflect on progress, analyze skill growth, or even remember what was done on a given day.

The challenge isn’t just organizational—it’s personal. Employees and learners alike need a natural, frictionless way to record their activities daily without feeling like it’s another administrative chore. Current tools for logging work or learnings are either too rigid, require manual effort, or aren’t conversational, making it easy to forget entries and lose valuable insights.

Workly addresses this by acting like a friendly, conversational partner with whom users can casually share their work and learning progress, which is then structured and stored over time for reflection and personal growth.

### Why Agents?

Agents are uniquely suited to this problem because they can actively engage users, understand natural language inputs, and autonomously process and organize information. A conversational agent can:

- Prompt users gently at a scheduled time to log their day.

- Understand free-form text and extract meaningful structured information (tasks, hours, skills learned).

- Persist data over time and generate summaries or insights without manual intervention.

- Act as a “personal assistant” rather than a static spreadsheet, making logging natural and effortless.

- Traditional timesheet or note-taking apps lack this proactive, interactive capability. 

By using agents, Workly becomes more than a tool—it becomes a personal companion without judgement for tracking growth.

**Overall architecture**

Workly is a multi-agent conversational system designed for personal work and learning tracking. Its architecture is modular, with specialized sub-agents that handle different tasks:

**1. Collector Agent**

-- Sends a daily prompt (e.g., 7 PM) asking the user about tasks completed and skills learned.

-- Receives user responses in natural language.

**2. Extraction Agent**

-- Parses user input to identify tasks, time spent, and skills or learnings.

-- Auto-detects the date for the entry.

**3. Storage Tool**

-- Saves structured entries to a CSV file, acting as persistent memory.

--Allows users to revisit their logs over time to reflect on personal growth.

**4. Summary Agent**

-- Generates weekly summaries highlighting trends in skills learned, topics explored, and task completion patterns.

**Workflow Overview:**

User → Collector Agent → Extraction Agent → Storage (CSV) → Summary Agent

This modular architecture ensures that Workly can handle daily inputs, organize them automatically, and provide insights over time.


### Demo 


Daily Interaction Example:

**Workly (7 PM):** “Hi! How was your day? What tasks did you complete and what did you learn?”

**User:**  “Today I automated ticket creation, fixed two bugs, and learned about async flows in Python.”

Structured CSV Entry:

| Date       | Task                          | Hours | Skills / Learnings          |
|------------|-------------------------------|-------|-----------------------------|
| 2025-12-01 | Automated ticket creation      | 2     | Workflow automation         |
| 2025-12-01 | Fixed bugs                     | 1     | Debugging                   |
| 2025-12-01 | Learned async flows in Python  | 1     | Async programming           |



Weekly Summary Example:

Total Hours Logged: 15

Skills Learned: Async programming, workflow automation, debugging

Highlights: Consistent daily logging, improvement in automation tasks

### The Build 

- Tools & Technologies Used:

         1. Agent Development Kit (ADK-Python) – Core framework for building multi-agent architecture.

         2. CSV Writer & Reader Tools – For structured storage of daily entries.

         3. Learning Tag Extractor – To automatically identify skills and topics in free-text logs.

         4. Date Utilities – Auto-detect the date for each entry.

         5. Sessions & Memory – CSV acts as persistent memory; weekly context maintained for summaries.

         6. Optional WhatsApp Integration via n8n – For sending daily prompts and receiving responses  conversationally.

- Implementation Highlights:

       1. Multi-agent system ensures clear separation of concerns: collection, extraction, storage, and summarization.

       2. Free-form text inputs are parsed to extract actionable insights.

       3. CSV-based memory simplifies persistence without complex databases.

       4. Summaries provide actionable insights for personal reflection on skill growth.

