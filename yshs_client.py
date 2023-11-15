"""
A client is a warpper with several chats
"""

from yshs import Client

client = Client()  # 注；一个Client可包含多个ChatThead, 一个ChatThead对应一个Conversation（根据chat_id区分），一个Conversation有多个轮次（turns）

prompt = "hello"  # user prompt
for chunk in client.send_prompt(prompt, chat_id=None):  # send_prompt()时自动创建ChatThead
    print(chunk['response'], end='', flush=True)
print()
chat_id = chunk['chat_id']
print(f'chat_id: {chat_id}')

prompt = 'who are you?'
for chunk in client.send_prompt(prompt, chat_id=chat_id):  # send_prompt()时自动匹配ChatThead，若不存在则创建
    print(chunk['response'], end='', flush=True)
print()
print(f'chat_id: {chat_id}')
