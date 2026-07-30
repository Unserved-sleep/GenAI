from crewai import Crew, Process

from agents import insurance_agent, summary_agent
from tasks import insurance_task, summary_task

insurance_crew = Crew(
    agents=[
        insurance_agent,
        summary_agent
    ],

    tasks=[
        insurance_task,
        summary_task
    ],

    process=Process.sequential,
    verbose=True
)