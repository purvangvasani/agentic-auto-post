# post_text = generate_post(topic, tone="authentic and reflective")
import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_post(topic, tone="friendly and insightful"):
    prompt = f"""You're a thought leader on LinkedIn. Write a short, engaging post with a {tone} tone based on the topic below:

    Topic: {topic}

    Requirements:
    - Keep under 300 words
    - Make it conversational, but professional
    - Include a question or call to action at the end
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()