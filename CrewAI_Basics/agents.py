from crewai import Agent, LLM
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model="gemini/gemini-3-flash-preview"
)

insurance_agent = Agent(
    role="Insurance Expert",
    goal="Answer insurance questions accurately.",
    backstory="""
    You are an experienced insurance consultant with years
    of experience helping customers understand policies.
    """,
    llm=llm,
    verbose=True
)

summary_agent = Agent(
    role="Insurance Summary Expert",
    goal="Summarize insurance information in simple language.",
    backstory="""
    You specialize in simplifying complex insurance
    information so customers can easily understand it.
    """,
    llm=llm,
    verbose=True
)