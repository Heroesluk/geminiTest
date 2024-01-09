import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part

import os

from flask import Flask

app = Flask(__name__)

def generate_text(project_id: str, location: str) -> str:
    # Initialize Vertex AI
    vertexai.init(project=project_id, location=location)
    # Load the model
    multimodal_model = GenerativeModel("gemini-pro-vision")
    # Query the model
    response = multimodal_model.generate_content(
        [
            # Add an example image
            Part.from_uri(
                "gs://generativeai-downloads/images/scones.jpg", mime_type="image/jpeg"
            ),
            # Add an example query
            "what is shown in this image?",
        ]
    )
    print(response)
    return response.text




@app.route('/')
def hello_world():
    return "Hello world"
@app.route('/ai')
def hello_world():
    return generate_text("ageless-webbing-405115", "us-west1")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))