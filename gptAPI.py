# --------------- Documentação 
# from openai import OpenAI
# client = OpenAI()

# response = client.responses.create(
#     model="gpt-4.1",
#     tools=[{"type": "web_search_preview"}],
#     input="What was a positive news story from today?"
# )

# print(response.output_text)



# --------------- Rocketseat
from openai import OpenAI
# import os
# os.environ['OPENAI_API_KEY'] = ""

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo", # mais barato
  max_tokens= 200, # limitar o número de tokens (um texto menor como resposta)
  temperature= 0.1, # quanto mais próximo de 1, mais criativas serão as respostas
  messages=[
    {"role": "system", "content": "You are a helpful assistant."}, # Persona: Serve para direcionar o modelo de linguagem sobre como ele deve se comportar. Ex: Haja como um especialista Backend em Python.
    {
        "role": "user",
        "content": "Write a haiku about recursion in programming." # Ordem do que o modelo de linguagem deve fazer
    }
  ]
)

print(completion.choices[0].message)