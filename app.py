import os
import openai
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Get OpenAI API key from environment variables
openai.api_key = os.getenv("BenedictMotha")

@app.route('/')
def home():
    return "AI Chatbot is running!"

@app.route('/ask', methods=['POST'])
def ask():
    # Get the question from the POST request
    data = request.get_json()
    user_input = data.get('question')

    if not user_input:
        return jsonify({'error': 'No question provided'}), 400

    try:
        # Use OpenAI's GPT model to generate a response
        response = openai.Completion.create(
            engine="text-davinci-003",  # Or another model of your choice
            prompt=user_input,
            max_tokens=150
        )

        # Extract the text response from OpenAI API
        bot_response = response.choices[0].text.strip()

        # Return the response as JSON
        return jsonify({'response': bot_response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
