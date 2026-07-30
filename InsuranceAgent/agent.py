from dotenv import load_dotenv
import os
from pydantic_ai import Agent, RunContext

from tools import (
    calculate_premium,
    get_policy_details,
    compare_policies,
    check_eligibility,
)

load_dotenv()
groq_key = os.getenv("GROQ_API_KEY")

insurance_agent = Agent(
    model="groq:llama-3.3-70b-versatile",
    system_prompt="""
    You are an insurance assistant.

    Always use the available tools whenever the user
    asks about premiums, policy information,
    comparisons or eligibility.

    Never make up policy information.
    """
)
@insurance_agent.tool
def premium_tool(
    ctx: RunContext[None],
    age: int,
) -> int:
    """
    Calculate insurance premium from customer age.
    """
    print("Premium Tool Called")
    return calculate_premium(age)

@insurance_agent.tool
def policy_lookup(
    ctx: RunContext[None],
    policy_name: str,
) -> str:
    """
    Retrieve insurance policy details.
    """
    print("Policy Lookup Called")
    return get_policy_details(policy_name)


@insurance_agent.tool
def policy_comparison(
    ctx: RunContext[None],
    policy1: str,
    policy2: str,
) -> str:
    """
    Compare two insurance policies.
    """
    print("Comparison Tool Called")
    return compare_policies(policy1, policy2)

@insurance_agent.tool
def eligibility_check(
    ctx: RunContext[None],
    age: int,
) -> str:
    """
    Check eligibility for insurance policies based on age.
    """
    print("Eligibility Check Called")
    return check_eligibility(age)