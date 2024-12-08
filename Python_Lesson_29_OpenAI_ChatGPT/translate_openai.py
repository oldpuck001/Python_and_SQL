# translate_openai.py

from openai import OpenAI

# 替換為你的 API 密鑰
api_key = input('your-api-key:')

client = OpenAI(api_key=api_key)

source_language = 'English'
target_language = 'Chinese'
text = 'Hello, how are you?'

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": f"You are a helpful assistant that translates text from {source_language} to {target_language}."},
        {"role": "user", "content": f"Translate the following text: {text}"}
    ]
)

translation = completion["choices"][0]["message"]["content"].strip()

print(f"Translated Text: {translation}")