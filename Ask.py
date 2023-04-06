def ChatGpt(speech):
  #> pip install openai
  import openai
  import OpenAI_Config

  openai.organization = OpenAI_Config.org_id
  openai.api_key = OpenAI_Config.api_key

  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": speech}],
    temperature=0,
    max_tokens=500,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )
  # print(response)
  content = response["choices"][0]["message"]["content"]
  # print(content)
  return content
