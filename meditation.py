import openai
openai.api_key = "YOUR_OPENAI_API_KEY"

def create_meditation_script(mood):
    prompt = f"Write a calming meditation script for someone feeling {mood}."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
