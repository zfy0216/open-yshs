---
tags: 教程
---

# 远上寒山调用模型教程

通过API-KEY调用LLM-3.5和4.0.

## 设置API-KEY

```bash
vi ~/.bashrc
# 添加一行
export YSHS_API_KEY="Fill in your API-KEY here"
# 保存后检查
source ~/.bashrc   # 刷新环境变量
echo $YSHS_API_KEY  # 如果输出你的API-KEY，则设置成功
```
注：尽量不要在代码中直接写入API-KEY，以免泄露。

## 列出可用模型

+ 安装yshs python包
```bash
pip install yshs
```

+ 列出模型：
```python
import os, sys
import yshs
yshs.api_key = os.getenv('YSHS_API_KEY')

response = yshs.Models.list(refresh=True, return_all_info=False)
print(response)
print(f'Number of models: {len(response)}')

# 输出：
['openai/gpt-3.5-turbo', 'openai/gpt-4']
Number of models: 2
```

## 调用模型


```python
import os, sys
import yshs
yshs.api_key = os.getenv('YSHS_API_KEY')  # 读取环境变量中的 API KEY并设置

def request_model(model, messages, engine=None, **kwargs):
    """统一的请求模型函数"""
    result = yshs.LLM.chat(
            model=model,  # 模型名称，例如 "openai/gpt-4", 可通过 list_models.py 查看可用模型
            engine=engine,  # 引擎名称, 可选参数，例如 "gpt-4-1106-preview"
            messages=messages,  # 一个会话的消息列表
            stream=True,  # 是否以流式的方式返回结果
            **kwargs  # 其他参数
        )

    full_result = ""
    for i in result:  # result 是一个生成器，每次迭代返回一个消息
        full_result += i
        sys.stdout.write(i)
        sys.stdout.flush()
    print()
    return full_result

def request_gpt35(messages):
    model = "openai/gpt-3.5-turbo"
    return request_model(model, messages=messages)

def request_gpt4(messages):
    model = "openai/gpt-4"
    engine = 'gpt-4-1106-preview'
    return request_model(model, messages=messages, engine=engine)

if __name__ == '__main__':
    system_prompt = "You are a helpful assistant."  # 系统提示词，指示模型扮演的角色和任务等
    prompt = "hello"  # 提示词，即用户输入的问题
    
    # messages代表1个对话，可能有多个轮次，对话有三种角色：system, user, assistant, 分别代表系统、用户、助手
    messages=[
            {"role": "system", "content": system_prompt},  # 设置系统提示词
            {"role": "user", "content": prompt},  # 设置用户输入第1个问题
            ## 如果有多轮对话，可以继续添加，"role": "assistant", "content": "Hello there! How may I assist you today?"
            ## 如果有多轮对话，可以继续添加，"role": "user", "content": "I want to buy a car."
        ]
    answer = request_gpt35(messages=messages)
    # answer = request_gpt4(messages=messages)

```

