from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/ask", methods=['POST'])
def ask():
    pass
    
    

