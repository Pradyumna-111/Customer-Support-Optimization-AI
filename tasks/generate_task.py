from crewai import Task
from agents.solution_agent import solution_agent
from tasks.classify_task import classification_task
from tasks.retreive_task import retrieval_task

generation_task = Task(
    description="""
    Using the classification report and the retrieved knowledge base context,
    compose a complete, customer-ready support response.

    Guidelines:
    1. Open by acknowledging the specific issue — reference the customer's own
       words to show you read their message carefully.
    2. Apologise if appropriate (Critical/High urgency or Furious/Frustrated
       sentiment) — be genuine, not formulaic.
    3. Provide the resolution:
       - Give clear, numbered step-by-step instructions where applicable.
       - Cite policies accurately (refund timelines, cancellation procedures, SLAs).
       - If the issue cannot be fully resolved in this message, clearly explain
         what will happen next and by when.
    4. If escalation is required (as flagged by the classifier), include the
       escalation path: who the customer will hear from, in what timeframe,
       and via which channel.
    5. Close with a warm, brand-appropriate sign-off that rebuilds confidence.
    6. Adjust tone to match sentiment:
       - Furious/Frustrated: extra empathy, lead with apology, avoid jargon
       - Neutral/Curious: professional and efficient
       - Satisfied: friendly and appreciative
    Do not invent policies, timelines, or facts not present in the retrieved context.
    """,

    expected_output="""
    A complete, professional customer support response ready to be sent,
    including:
    - Personalised opening acknowledging the issue
    - Clear resolution steps or next-action plan
    - Relevant policy information stated accurately
    - Escalation details if required
    - Warm closing statement
    The response should be 150-400 words depending on complexity.
    """,

    context=[classification_task, retrieval_task],
    agent=solution_agent
)
