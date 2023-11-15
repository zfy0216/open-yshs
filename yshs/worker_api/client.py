"""
a client is a wrapper with several chat threads
"""

import damei as dm 
from yshs.worker_api.chat_thread import ChatThead

import uuid
logger = dm.get_logger('client.py')


class Client:
    def __init__(self) -> None:
        self.chat_threads = dict()

    def create_chat_thread(self, chat_id=None, **kwargs):
        """
        Create a new chat thread
        :param chat_id: the chat thread id
        :param model: the model name
        :param system_prompt: the system prompt
        return: a ChatThead object
        """
        if chat_id in self.chat_threads:
            raise ValueError(f"Chat thread {chat_id} already exists")
        chat_id = chat_id if chat_id else str(uuid.uuid4())[:8]
        logger.info(f"Create a new chat thread with chat_id {chat_id}")
        chat_thread = ChatThead(chat_id=chat_id, **kwargs)
        self.chat_threads[chat_id] = chat_thread
        return chat_thread
    
    def remove_chat_thread(self, chat_id):
        """
        Remove a chat thread
        :param chat_id: the chat thread id
        """
        if not chat_id in self.chat_threads:
            raise ValueError(f"Chat thread {chat_id} does not exist")
        logger.info(f"Remove chat thread {chat_id}")
        del self.chat_threads[chat_id]
    
    def get_chat_thread(self, chat_id=None, **kwargs):
        if chat_id in self.chat_threads:
            return self.chat_threads[chat_id]
        chat_id = chat_id if chat_id else str(uuid.uuid4())[:8]
        logger.info(f"Create a new chat thread with chat_id {chat_id}")
        chat_thread = ChatThead(chat_id=chat_id, **kwargs)
        self.chat_threads[chat_id] = chat_thread
        return chat_thread
        
    def send_prompt(self, prompt, chat_id=None, **kwargs):
        """
        :param prompt: the last question
        :chat_id: the chat thread id
        :model: the model name

        """
        chat_thread = self.get_chat_thread(chat_id=chat_id, **kwargs)
        return chat_thread.send_prompt(prompt, **kwargs)