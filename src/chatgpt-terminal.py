import openai
import prompt_toolkit

# insert openai api key here
openai.api_key = ""

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()
    return message

while True:
    try:
        prompt = prompt_toolkit.prompt('> ')
        response = generate_response(prompt)
        print(response)
    except KeyboardInterrupt:
        break
