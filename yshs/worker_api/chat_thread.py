

import os, sys
from pathlib import Path
here = Path(__file__).parent
import uuid
try:
    from yshs.worker_api.chat import ChatModel
except:
    sys.path.append(str(here.parent.parent))
    from yshs.worker_api.chat import ChatModel

import damei as dm
logger = dm.get_logger('chat_thread.py')

class ChatThead:
    """A chat thread is a continuous conversation with chat_id and history"""

    def __init__(self, model=None, chat_id=None, system_prompt="You are a helpful assistant.", **kwargs) -> None:
        # chat_id with 8 chars is a unique id for a chat thread
        self.chat_id = str(uuid.uuid4())[:8] if chat_id is None else chat_id
        self.model = model if model else "openai/gpt-3.5-turbo"
        self.engine = kwargs.pop("engine", None)
        self.system_prompt = system_prompt
        self.messages = [
            {"role": "system", "content": system_prompt},  # 设置系统提示词
        ]
        logger.info(f"A chat thread is created, chat_id {self.chat_id}, model: {self.model}, system_prompt: {self.system_prompt}")


    def send_prompt(self, prompt, **kwargs):
        """
        :param message: the last question
        """
        self.messages.append(
            {"role": "user", "content": prompt})
        
        generator = ChatModel.chat(
            model=self.model,
            engine=self.engine,
            messages=self.messages,
            stream=True,
        )

        full_result = ""
        for i in generator:
            full_result += i
            chunk = {
                "chat_id": self.chat_id,
                "response": i,
            }
            yield chunk
        self.messages.append(
            {"role": "assistant", "content": full_result})
        

if __name__ == '__main__':
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


    

