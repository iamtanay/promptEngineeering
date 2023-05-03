import time
import setup
import openai

openai.api_key = setup.OPENAI_API_KEY

def get_completion(prompt, model="gpt-3.5-turbo"):
    try:

        response = openai.ChatCompletion.create(
        model=model,
        messages = [{"role": 'system', "content": f'{prompt}'}]
        )
        resp = response["choices"][0]["message"]["content"]
        return resp


    except openai.error.RateLimitError as e:

        retry_time = e.retry_after if hasattr(e, 'retry_after') else 30
        print(f"Rate limit exceeded. Retrying in {retry_time} seconds...")
        time.sleep(retry_time)
        return get_completion(prompt)

text = f"""
You should express what you want a model to do by \ 
providing instructions that are as clear and \ 
specific as you can possibly make them. \ 
This will guide the model towards the desired output, \ 
and reduce the chances of receiving irrelevant \ 
or incorrect responses. Don't confuse writing a \ 
clear prompt with writing a short prompt. \ 
In many cases, longer prompts provide more clarity \ 
and context for the model, which can lead to \ 
more detailed and relevant outputs.
"""
prompt = f"""
Summarize the text delimited by triple backticks \ 
into a single sentence.
```{text}```
"""
response = get_completion(prompt)
print(response)