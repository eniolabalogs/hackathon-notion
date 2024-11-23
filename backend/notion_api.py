import requests
import os

NOTION_API_URL = "https://api.notion.com/v1"
NOTION_TOKEN = os.getenv("NOTION_TOKEN")

def create_notion_workspace(content):
    """
    Create a new Notion page or database and populate it with content.
    """
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    # Example: Create a Notion page
    page_data = {
        "parent": {"type": "page_id", "page_id": "your_parent_page_id"},
        "properties": {
            "title": [
                {"type": "text", "text": {"content": content["title"]}}
            ]
        },
        "children": content["children"]  # Content from AI
    }

    response = requests.post(f"{NOTION_API_URL}/pages", json=page_data, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Notion API Error: {response.text}")
