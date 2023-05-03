#########################################################
#
#
# In this file we learn how to transform the text
#
#
#########################################################

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

#########################################################
#
#
# 1. Identifying language
#
#
#########################################################
prompt = f"""
Tell me which language this is: 
```Combien coûte le lampadaire?```
"""
response = get_completion(prompt)
print(response)

#########################################################
#
#
# 2. Translating to other language
#
#
#########################################################
prompt = f"""
Translate the following English text to Spanish: \ 
```Hi, I would like to order a blender```
"""
response = get_completion(prompt)
print(response)

#########################################################
#
#
# 3. Changing the tone of the text
#
#
#########################################################
prompt = f"""
Translate the following from slang to a business letter: 
'Dude, This is Joe, check out this spec on this standing lamp.'
"""
response = get_completion(prompt)
print(response)

data_json = { "resturant employees" :[ 
    {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
    {"name":"Bob", "email":"bob32@gmail.com"},
    {"name":"Jai", "email":"jai87@gmail.com"}
]}

#########################################################
#
#
# 4. Changing the format
#
#
#########################################################
prompt = f"""
Translate the following python dictionary from JSON to an HTML \
table with column headers and title: {data_json}
"""
response = get_completion(prompt)
print(response)

#########################################################
#
#
# 5. Spell/Grammar check and proofreading
#
#
#########################################################
text = f"""
Got this for my daughter for her birthday cuz she keeps taking \
mine from my room.  Yes, adults also like pandas too.  She takes \
it everywhere with her, and it's super soft and cute.  One of the \
ears is a bit lower than the other, and I don't think that was \
designed to be asymmetrical. It's a bit small for what I paid for it \
though. I think there might be other options that are bigger for \
the same price.  It arrived a day earlier than expected, so I got \
to play with it myself before I gave it to my daughter.
"""
prompt = f"proofread and correct this review: ```{text}```"
response = get_completion(prompt)
print(response)