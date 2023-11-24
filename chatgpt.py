import os
from openai import OpenAI


def chatgpt_response(prompt, model="text-davinci-003"):
    response = OpenAI(api_key=os.environ['OPENAI_KEY']).completions.create(
        model=model,
        prompt=prompt,
        max_tokens=3500
    )

    return response.choices[0].text
