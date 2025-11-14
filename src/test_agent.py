import uuid
from agent import agent_reply

thread_id = str(uuid.uuid4())

# First interaction in a new thread
user_input_1 = "Hi, my name is Alex. What is a good programming joke?"
response_1 = agent_reply(user_input_1, thread_id)
for step in response_1:
    print(f"AI Response: {step}")

# Second interaction in the same thread
# The AI remembers the name "Alex" because of the InMemorySaver checkpointer
user_input_2 = "What did I just say my name was?"
response_2 = agent_reply(user_input_2, thread_id)
for step in response_2:
    print(f"AI Response: {step}")

# Third interaction to demonstrate tool calling
user_input_3 = "What is the weather is SF?"
response_3 = agent_reply(user_input_3, str(uuid.uuid4()))
for step in response_3:
    print(f"Tool Response: {step}")
