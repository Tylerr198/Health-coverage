from flask import Flask, jsonify, request, flash
from prompt import ask_prompt
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
CORS(app)

app.secret_key = os.urandom(24)

@app.route("/")
def home():
    return "<h1> Home Page </h1>"

@app.route("/ask", methods=['POST'])
def ask():
    data = request.json
    prompt = data.get("prompt").get("ask")
    ai_response = ask_prompt(prompt)
    return jsonify({'message': ai_response}), 200

# hanlde PDF upload
UPLOAD_FOLDER = './data'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        print("File request:", request.files)
        if 'file' not in request.files:
            flash('No file part')
            return jsonify({'message': 'No file found'}), 400
        file = request.files['file']
        print("file name:", file)
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return jsonify({'message': 'No selected file'}), 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return jsonify({'message': 'Successful Upload'}), 200



    
    

