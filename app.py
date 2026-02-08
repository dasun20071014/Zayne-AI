from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

# Your Groq API Key
GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_api():
    user_msg = request.json.get("message")
    try:
        # Using Llama-3.3-70b model for high quality and speed
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are Zayne AI, a helpful and smart assistant."
                },
                {
                    "role": "user",
                    "content": user_msg,
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        
        response_text = chat_completion.choices[0].message.content
        return jsonify({"response": response_text})
    
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

@app.route('/clear', methods=['POST'])
def clear_chat():
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
