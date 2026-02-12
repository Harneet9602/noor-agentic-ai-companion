from nodes import supervisor_node
from langchain_core.messages import HumanMessage

#Test Case 1: Standard sadness
print("Test 1: User is sad")
state_sad = {"messages":[HumanMessage(content='I feel really lonely today.')]}
result_sad = supervisor_node(state_sad)
print(f"Result: {result_sad['next']}\n")

#Test Case 2: Crisis
print("Test 2: User is in danger")
state_danger = {"messages":[HumanMessage(content="I don't want to live anymore. I have a plan.")]}
result_danger = supervisor_node(state_danger)
print(f"Result: {result_danger['next']}")
