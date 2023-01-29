import os
import openai
openai.organization = "org-t8hM3GwLc423J1x5SR0jLJSx"
openai.api_key = "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"

engines = openai.Engine.list()

def ask_question(user_input: str):
    # post https://api.openai.com/v1/completions
    question = f"{user_input} \nA:"
    completion = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        temperature=0,
        max_tokens=50,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    return completion
    
completion = ask_question("What is the tempature of sun")
print(completion["choices"][0]["text"])