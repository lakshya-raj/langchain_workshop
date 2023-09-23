from flask import Flask
from langchain.llms import OpenAI
from env import OPENAI_API_KEY
from requests import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.post('/chat')
def chat():
    question = request.json['question']
    llm = OpenAI(OPENAI_API_KEY)
    return llm.predict(question)

# if __name__ == '__main__':
#     app.run()