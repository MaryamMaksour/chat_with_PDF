from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok

from app import ask
from Summarizing import summary
from translate import translate
from Assistant import ask_assistant

api = Flask(__name__)
run_with_ngrok(api)

@api.route('/',methods=['GET', 'POST'])
def chat():
    d = {}
    data = str(request.args['message'])
    answer = str(ask(data))
    d['answer'] = answer
    return d


@api.route('/summary', methods=['GET', 'POST'])
def summar():
        d = {}
        file = str(request.args['file'])
        answer = ""
        answer = str(summary(file))
        d['answer'] = answer
        return d
    
    
    
@api.route('/translatePDF',  methods=['GET', 'POST'])
def trans_PDF():
    d = {}
    file = str(request.args['file'])
    answer = str(translate(file))
    d['answer'] = answer
    return d



@api.route('/assistant', methods=['GET', 'POST'])
def assistant():
    d = {}
    file = str(request.args['message'])
    answer = str(ask_assistant(file))
    d['answer'] = answer
    return d

if __name__ == '__main__':
    api.run()


