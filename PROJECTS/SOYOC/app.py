from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:1b"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_prompt = data.get("message", "")
    
    payload = {
        "model": MODEL_NAME,
        "prompt": user_prompt,
        "stream": False
    }

    try:
        ollama_response = requests.post(OLLAMA_URL, json=payload)
        if ollama_response.status_code == 200:
            result = ollama_response.json()
            return jsonify({"response": result["response"]})
        else:
            return jsonify({"response": f"Error from Ollama: {ollama_response.status_code}"}), 500
    except Exception as e:
        return jsonify({"response": f"Server error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)


