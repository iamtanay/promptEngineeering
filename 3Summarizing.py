#########################################################
#
#
# In this file we learn how to summarize and make the
# summary better with each prompt.
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

prod_review = """
Got this panda plush toy for my daughter's birthday, \
who loves it and takes it everywhere. It's soft and \ 
super cute, and its face has a friendly look. It's \ 
a bit small for what I paid though. I think there \ 
might be other options that are bigger for the \ 
same price. It arrived a day earlier than expected, \ 
so I got to play with it myself before I gave it \ 
to her.
"""

#########################################################
#
#
# 1. Generating a summary of the review by limiting the
# word count
#
#
#########################################################
prompt = f"""
Your task is to generate a short summary of a product \
review from an ecommerce site. 

Summarize the review below, delimited by triple 
backticks, in at most 30 words. 

Review: ```{prod_review}```
"""

response = get_completion(prompt)
print(response)

#########################################################
#
#
# 2. Focusing on specific topics of the review
#
#
#########################################################
############### Shipping and delivery ###################
prompt = f"""
Your task is to generate a short summary of a product \
review from an ecommerce site to give feedback to the \
Shipping deparmtment. 

Summarize the review below, delimited by triple 
backticks, in at most 30 words, and focusing on any aspects \
that mention shipping and delivery of the product. 

Review: ```{prod_review}```
"""

response = get_completion(prompt)
print("Focusing on shipping and delivery: ")
print(response)

############### Price and delivery ###################
prompt = f"""
Your task is to generate a short summary of a product \
review from an ecommerce site to give feedback to the \
pricing deparmtment, responsible for determining the \
price of the product.  

Summarize the review below, delimited by triple 
backticks, in at most 30 words, and focusing on any aspects \
that are relevant to the price and perceived value. 

Review: ```{prod_review}```
"""

response = get_completion(prompt)
print("Focusing on price and value: ")
print(response)

#########################################################
#
#
# 3. Extracting v/s summarizing
#
#
#########################################################
prompt = f"""
Your task is to extract relevant information from \ 
a product review from an ecommerce site to give \
feedback to the Shipping department. 

From the review below, delimited by triple quotes \
extract the information relevant to shipping and \ 
delivery. Limit to 30 words. 

Review: ```{prod_review}```
"""

response = get_completion(prompt)
print(response)