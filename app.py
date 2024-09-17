from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import pymongo
from fuzzywuzzy import process
from transformers import pipeline
import os

app = Flask(__name__)
CORS(app)

# Load environment variables only in development mode
if os.environ.get("FLASK_ENV") != "production":
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ModuleNotFoundError:
        print("python-dotenv not installed, skipping load_dotenv")
    
# MongoDB setup
mongo_url = os.getenv('MONGO_URL')
client = pymongo.MongoClient(mongo_url)
db = client['test']
collection = db['policies']

# Load data into a DataFrame
data = pd.DataFrame(list(collection.find()))

# Initialize the question-answering pipeline
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

@app.route('/')
def home():
    return 'Hello World'

@app.route('/qahandbook/<query>', methods=['POST'])
def get_policy_answer(query):
    df = data
    try:
        # Fuzzy search for policy
        return jsonify({'policy': search_policy_fuzzy(df, query), 'description': '  Description of the policy...'})
    except Exception as e:
        # Fallback to QA pipeline if fuzzy search fails
        answer = answer_question(df, query)
        return jsonify({'policy': query, 'description': answer})

def search_policy_fuzzy(data, query):
    best_match = process.extractOne(query, data['policy'].tolist())
    if best_match:
        return data[data['policy'] == best_match[0]]['description'].values[0]
    else:
        return "No relevant policy found."

def answer_question(data, question):
    for context in data['description'].tolist():
        result = qa_pipeline({'question': question, 'context': context})
        if result['score'] > 0.2:  # Confidence threshold
            return result['answer']
    return "No relevant policy found."

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)
