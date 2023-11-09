
import os, sys
import yshs
from yshs.version import __appname__
import requests
from ..worker_api.chat import ChatModel

class Models:

    def __init__(self) -> None:
        pass

    @staticmethod
    def chat(*args, **kwargs):
        return ChatModel.chat(*args, **kwargs)
    
    @staticmethod
    def ensure_api_key(api_key):
        if api_key is None:
            api_key = os.environ.get(f"{__appname__.upper()}_API_KEY", None)
        if api_key is None:
            raise ValueError(f"""            
The API-KEY is required. You can set it via `{__appname__.lower}.api_key=xxx` in your code, or set the environment variable `{__appname__.upper()}_API_KEY` via `export HEPAI_API_KEY=xxx`.
Alternatively, it can be provided by passing in the `api_key` parameter when calling the method.
""")
        return api_key
    
    @staticmethod
    def list(**kwargs):
        """
        List all models on HepAI Platform.
        :param refresh: Whether to refresh the model list, default is False.
        :param return_all_info: Whether to return all information of the models, default is False.
        :param api_key: Your HepAI api key, can be obtained in https://ai.ihep.ac.cn, only return public models if not provided.
        :return: The list of models.
        """  
        api_key = kwargs.pop("api_key", None) or yshs.api_key
        api_key = Models.ensure_api_key(api_key)
        
        url = kwargs.pop("url", None)
        if not url:
            host = kwargs.pop("host", "www.yshs.vip")
            port = kwargs.pop("port", None)
            if port:
                url = f"http://{host}:{port}"
            else:
                url = f'https://{host}'
        assert url, f'url or (host and port) is required. For example: url="http://aiapi.ihep.ac.cn:42901"'

        ret = requests.post(
            f"{url}/list_models",
            headers={"Authorization": f"Bearer {api_key}"},
            json=kwargs,
            )
        if ret.status_code != 200:
            raise ValueError(f"Hai Model connect url: {url} Error: \n{ret.status_code} {ret.reason} {ret.text}")
        return ret.json()


