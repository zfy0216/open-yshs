
import os, sys
import yshs
yshs.api_key = os.getenv('YSHS_API_KEY')


def request_model(model, system_prompt, prompt, **kwargs):
    responese = yshs.LLM.chat(
        model=model,  # 选择模型
        messages=[
          {"role": "system", "content": system_prompt},  # 系统提示
          {"role": "user", "content": prompt},  # 第一个问题
          # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},  # 第一个的答案
          # {"role": "user", "content": "Where was it played?"}  # 第二个问题
        ],
        **kwargs,
    )

    full_response = ""
    for x in responese:
        sys.stdout.write(x)  # 逐token输出
        sys.stdout.flush()
        full_response += x
    print()
    return full_response

def request_gpt35():
    model = "openai/gpt-3.5-turbo"
    system_prompt = "You are a helpful assistant."
    prompt = "Who won the world series in 2020?"
    return request_model(model, system_prompt, prompt)

def request_gpt4():
    model = "openai/gpt-4"
    system_prompt = "You are a helpful assistant."
    prompt = "Who won the world series in 2020?"
    return request_model(model, system_prompt, prompt)

answer = request_gpt35()
# print(answer)
# answer = request_gpt4()