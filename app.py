import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import random
from flask import Flask, request, jsonify
from comment import generate_comments

app = Flask(__name__)

@app.route('/generate_comments', methods=['POST'])
def generate_comments_route():
    data = request.json
    text = data.get('text')
    comments = generate_comments(text)
    return jsonify(comments)

if __name__ == '__main__':
    app.run(debug=True)
