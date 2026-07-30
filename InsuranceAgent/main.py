from agent import insurance_agent

while True:

    query = input("\nYou : ")

    if query.lower() == "exit":
        break

    result = insurance_agent.run_sync(query)

    print("\nAgent :", result.output)