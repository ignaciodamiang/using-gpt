from dotenv import load_dotenv
import openai
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_gpt(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.5,
            max_tokens=2000
        )
        message = response.choices[0].text
    except Exception as e:
        message = f"Error: {str(e)}"
    return message.strip()

while True:
    prompt = input("You: ")
    if prompt.lower() == "exit":
        break
    message = ask_gpt(prompt)
    print("Bot:", message)
