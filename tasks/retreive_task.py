from crewai import Task
from agents.kb_agent import kb_agent
from tasks.classify_task import classification_task

retrieval_task = Task(
    description="""
    Using the classification report produced by the classifier agent, retrieve
    all information needed to resolve the customer's issue.

    Steps:
    1. Read the Issue Category, Sub-category, and Core Problem Summary from the
       classification report.
    2. Search the knowledge base for support articles and FAQs matching the issue.
    3. Look up historical tickets with the same category and sub-category to find
       proven resolutions.
    4. Retrieve the relevant policy document (refund policy, cancellation policy,
       SLA, etc.) applicable to this issue type.
    5. Check if any known bugs, outages, or product limitations match the
       described symptoms.
    6. Rank all retrieved items by relevance to this specific ticket and discard
       anything with low relevance.
    7. Produce a concise context summary that the solution agent can use directly.
    """,

    expected_output="""
    A ranked retrieval report containing:
    - Top 3 relevant knowledge base articles or FAQ entries (title + key points)
    - Applicable policy excerpt (verbatim or paraphrased accurately)
    - Similar past ticket resolutions (up to 2, with steps that worked)
    - Any known bugs or outages relevant to the issue (if applicable)
    - A short context summary (3-5 sentences) synthesising the above for the
      solution agent
    """,

    context=[classification_task],
    agent=kb_agent
)
