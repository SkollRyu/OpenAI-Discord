import os
import openai
openai.organization = "org-t8hM3GwLc423J1x5SR0jLJSx"
openai.api_key = "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"

engines = openai.Engine.list()

# post https://api.openai.com/v1/completions
completion = openai.Completion.create(
  model="text-davinci-003",
  prompt="Where is the Valley of Kings?\nA:",
  temperature=0,
  max_tokens=10,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\n"]
)

print(completion["choices"][0]["text"])