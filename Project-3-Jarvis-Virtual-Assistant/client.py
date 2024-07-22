from openai import OpenAI

client = OpenAI(
    api_key="sk-proj-G1vjTuKPTqTLEyByitd4T3BlbkFJYvCZkKIrIK79z8dsymuG",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)