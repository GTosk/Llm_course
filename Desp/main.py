from openai import OpenAI
import os
import chainlit as cl

os.environ["OPENAI_API_KEY"] = os.environ['repl_openai_api_key']

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


@cl.on_message
async def main(message : str):
  response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  messages=[
    {
      "role": "system",
      "content": "You are an assistant who is in love with 'Δέσποινα' and always says how much he loves her, how beautiful and perfect she is and other loving things about her."
    },
    {
      "role": "user",
      "content": message.content
    }
  ],
  temperature=1.31,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.23,
  presence_penalty=0.37
)


  await cl.Message(content = response.choices[0].message.content).send()





