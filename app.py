from flask import Flask,render_template, request, jsonify
from textblob import TextBlob
import nltk

nltk.download('punkt')

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/correct', methods=['POST'])
def correct_text():
    data = request.json
    text = data.get('text', '')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
   # Correct the spelling
    blob = TextBlob(text)
    corrected_text = str(blob.correct())

    return jsonify({
        "original": text,
        "corrected": corrected_text
    })

if __name__ == '__main__':
    app.run(debug=True)