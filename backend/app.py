from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from notion_api import create_notion_workspace
from ai_api import generate_content

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

@app.route("/")
def home():
    return {"status": "Backend is running!"}

# Endpoint: Generate and send project to Notion
@app.route("/generate", methods=["POST"])
def generate():
    try:
        # Get user input from request
        data = request.json
        project_description = data.get("description")

        if not project_description:
            return jsonify({"error": "Description is required"}), 400

        # Step 1: Use AI to generate content
        generated_content = generate_content(project_description)

        # Step 2: Send generated content to Notion
        notion_response = create_notion_workspace(generated_content)

        return jsonify({"success": True, "notion_response": notion_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
