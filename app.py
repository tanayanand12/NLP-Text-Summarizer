# Project Structure
# /nlp-text-summarizer
#   ├── app.py
#   ├── requirements.txt
#   ├── templates/
#   │   └── index.html
#   ├── static/
#   │   └── styles.css
#   └── README.md

# app.py
from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load pre-trained summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.json.get('text', '')
    
    # Check text length
    if len(text) < 50:
        return jsonify({"error": "Text is too short to summarize"})
    
    # Generate summary
    try:
        summary = summarizer(text, 
                             max_length=130, 
                             min_length=30, 
                             do_sample=False)[0]['summary_text']
        return jsonify({"summary": summary})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)