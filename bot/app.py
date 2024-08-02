from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)
nlp = spacy.load('en_core_web_sm')

def analyze_query(query):
    doc = nlp(query)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def get_financial_advice(query):
    entities = analyze_query(query)
    advice = "Here's what I found regarding your query:"
    
    # Example logic for financial advice
    if "investment" in query.lower():
        advice += "\nConsider diversifying your investments to reduce risk."
    elif "saving" in query.lower():
        advice += "\nIt's a good practice to save at least 20% of your income."
    elif "loan" in query.lower():
        advice += "\nEnsure you have a good credit score before applying for a loan."
    else:
        advice += "\nPlease provide more details for specific advice."

    return advice

@app.route('/')
def home():
    return "Hello! This is the bank's financial advice chatbot."

@app.route('/chat', methods=['POST'])
def chat():
    user_query = request.json.get('query')
    response = get_financial_advice(user_query)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True, port=8000)  # Changed port to 8000
