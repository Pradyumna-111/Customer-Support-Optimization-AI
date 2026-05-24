from crewai import Crew

from agents.classifier_agent import classifier_agent
from agents.kb_agent import kb_agent
from agents.solution_agent import solution_agent
from agents.qa_agent import qa_agent

from tasks.classify_task import classification_task
from tasks.retreive_task import retrieval_task
from tasks.generate_task import generation_task
from tasks.qa_task import qa_task

crew = Crew(
    agents=[
        classifier_agent,
        kb_agent,
        solution_agent,
        qa_agent
    ],

    tasks=[
        classification_task,
        retrieval_task,
        generation_task,
        qa_task
    ],

    verbose=True
)