# This code is for v1 of the openai package: pypi.org/project/openai
from openai import OpenAI
client = OpenAI()

response = client.completions.create(
  model="gpt-3.5-turbo",
  prompt="",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)