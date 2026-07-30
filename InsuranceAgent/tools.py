POLICIES = {
    "Health Shield": {
        "coverage": "₹10 Lakhs",
        "premium": "₹8,000/year",
        "waiting_period": "2 Years",
        "description": "Individual health insurance with hospitalization coverage."
    },

    "Family Protect": {
        "coverage": "₹20 Lakhs",
        "premium": "₹12,000/year",
        "waiting_period": "1 Year",
        "description": "Family floater plan covering spouse and children."
    },

    "Senior Care": {
        "coverage": "₹15 Lakhs",
        "premium": "₹18,000/year",
        "waiting_period": "3 Years",
        "description": "Specialized plan for senior citizens."
    }
}


def calculate_premium(age: int) -> int:
    if age < 30:
        return 5000
    elif age < 45:
        return 8000
    elif age < 60:
        return 12000
    return 18000


def get_policy_details(policy_name: str) -> str:
    policy = POLICIES.get(policy_name)

    if not policy:
        return "Policy not found."

    return (
        f"{policy_name}\n"
        f"Coverage: {policy['coverage']}\n"
        f"Premium: {policy['premium']}\n"
        f"Waiting Period: {policy['waiting_period']}\n"
        f"Description: {policy['description']}"
    )


def compare_policies(policy1: str, policy2: str) -> str:

    p1 = POLICIES.get(policy1)
    p2 = POLICIES.get(policy2)

    if not p1 or not p2:
        return "One or both policies not found."

    return (
        f"{policy1}\n"
        f"Coverage: {p1['coverage']}\n"
        f"Premium: {p1['premium']}\n\n"
        f"{policy2}\n"
        f"Coverage: {p2['coverage']}\n"
        f"Premium: {p2['premium']}\n\n"
        "Recommendation:\n"
        "Choose the policy based on your budget and coverage requirements."
    )


def check_eligibility(age: int) -> str:

    if age >= 60:
        return "Eligible for Senior Care."

    return "Eligible for regular Health Shield and Family Protect plans."