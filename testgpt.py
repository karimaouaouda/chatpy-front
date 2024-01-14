from openai import OpenAI

API_KEY = "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"
client = OpenAI(api_key=API_KEY)




response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "python send post request?"}
  ]
)

print(response.choices.pop(0).message.content)