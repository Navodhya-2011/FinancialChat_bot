import requests

def get_financial_advice(query):
    response = requests.post('http://127.0.0.1:8000/chat', json={"query": query}) 
    return response.json().get('response')

if __name__ == '__main__':
    print("Welcome to the financial advice chatbot!")
    while True:
        query = input("Enter your financial query (or 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        advice = get_financial_advice(query)
        print(advice)
