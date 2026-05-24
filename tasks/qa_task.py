from crewai import Task
from agents.qa_agent import qa_agent
from tasks.classify_task import classification_task
from tasks.retreive_task import retrieval_task
from tasks.generate_task import generation_task

qa_task = Task(
    description="""
    Perform a full quality assurance review of the drafted customer response
    against the original ticket, classification report, and retrieved context.

    Review checklist:
    1. Factual Accuracy
       - Every policy, timeline, and procedure cited matches the retrieved context.
       - No hallucinated information (invented order IDs, wrong refund periods, etc.).
    2. Completeness
       - All issues raised in the ticket are addressed — not just the primary one.
       - If escalation was flagged, escalation language and next steps are present.
    3. Tone and Empathy
       - Tone matches the customer's sentiment as classified.
       - No cold, generic, or dismissive language.
       - No over-promising or under-promising.
    4. Professionalism
       - Correct grammar, punctuation, and sentence structure throughout.
       - Appropriate formatting (numbered steps where needed, no walls of text).
    5. Compliance and Safety
       - No disclosure of internal system names, agent names, or confidential data.
       - No language that creates legal liability or violates company policy.
       - No statements that contradict official policy.
    6. Brand Voice
       - Response reflects a professional, empathetic, customer-first brand.

    If the response passes all checks: output the final approved response verbatim.
    If it fails any check: output a detailed revision request listing each issue
    with the exact line and the required correction.
    """,

    expected_output="""
    Either:
    A) APPROVED — the final, validated customer response exactly as it should be sent.
    B) REVISION REQUIRED — a numbered list of specific issues with exact corrections
       needed, followed by the corrected full response.
    """,

    context=[classification_task, retrieval_task, generation_task],
    agent=qa_agent
)
