import requests
import os

AI_API_URL = "https://api.openai.com/v1/completions"
AI_API_KEY = os.getenv("AI_API_KEY")

def generate_content(description):
    """
    Use AI to generate structured content based on the user's description.
    """
    headers = {
        "Authorization": f"Bearer {AI_API_KEY}",
        "Content-Type": "application/json"
    }

    # Example OpenAI request
    payload = {
        "model": "text-davinci-003",
        "prompt": f"Generate a structured plan for: {description}",
        "temperature": 0.7,
        "max_tokens": 300
    }

    response = requests.post(AI_API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        # Parse AI response
        ai_response = response.json()
        return {"title": description, "children": ai_response["choices"][0]["text"]}
    else:
        raise Exception(f"AI API Error: {response.text}")
