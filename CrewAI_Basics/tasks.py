from crewai import Task
from agents import insurance_agent, summary_agent

insurance_task = Task(
    description="""
    Explain what Health Shield insurance is and who should buy it.
    """,

    expected_output="""
    A clear explanation of the policy, its benefits,
    and the type of customer it is suitable for.
    """,

    agent=insurance_agent
)


summary_task = Task(
    description="""
    Read the insurance explanation provided by the previous task
    and summarize it in 5 concise bullet points.
    """,

    expected_output="""
    Five easy-to-understand bullet points summarizing the policy.
    """,

    agent=summary_agent,
    context=[insurance_task]
)