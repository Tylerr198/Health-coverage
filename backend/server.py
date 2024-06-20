from flask import Flask, jsonify, request
from prompt import ask_prompt
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "<h1> Home Page </h1>"

@app.route("/ask", methods=['POST'])
def ask():
    data = request.json
    prompt = data.get("prompt").get("ask")
    ai_response = ask_prompt(prompt)
    return jsonify({'message': ai_response}), 200
    
    

