from crewai import Task
from agents.classifier_agent import classifier_agent

classification_task = Task(
    description="""
    Analyze the following customer support ticket and produce a structured
    classification report.

    Ticket:
    {ticket}

    Your classification must include:
    1. Issue Category — choose the single best fit from:
       Billing, Technical, Account Access, Cancellation, Shipping, General Inquiry,
       Feature Request, or Other (specify).
    2. Sub-category — a more specific label within the category
       (e.g. "Billing > Duplicate Charge", "Technical > App Crash on Upload").
    3. Urgency Level — one of: Critical / High / Medium / Low.
       Criteria:
       - Critical: financial loss, data breach, legal threat, complete service outage
       - High: major feature broken, repeated failed contacts, threat to churn or dispute
       - Medium: partial functionality issue, billing confusion without loss
       - Low: general inquiry, feature request, minor UX complaint
    4. Customer Sentiment — one of: Furious / Frustrated / Neutral / Curious / Satisfied.
    5. Escalation Required — Yes or No, with a one-sentence justification.
    6. Core Problem Summary — one sentence describing the root issue for downstream agents.
    7. Key entities — list any product names, order IDs, dates, or amounts mentioned.
    """,

    expected_output="""
    A structured classification report with clearly labelled sections:
    - Category & Sub-category
    - Urgency Level (with brief reasoning)
    - Customer Sentiment
    - Escalation Required (Yes/No + justification)
    - Core Problem Summary
    - Key Entities
    """,

    agent=classifier_agent
)
