
"""
A chat thread is a continuous conversation with chat_id and history"
"""

from yshs import ChatThead

chat_thread = ChatThead(
    model="openai/gpt-3.5-turbo",  # "openai/gpt-3.5-turbo" or "openai/gpt-4"
    system_prompt="You are a helpful assistant.",  # system prompt
    )

prompt = "hello"  # user prompt
for chunk in chat_thread.send_prompt(prompt):
    print(chunk['response'], end='', flush=True)
print("\n")

prompt = 'who are you?'
for chunk in chat_thread.send_prompt(prompt):
    print(chunk['response'], end='', flush=True)
print("\n")





