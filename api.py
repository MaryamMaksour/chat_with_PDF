from flask import Flask, request, jsonify
from app import ask
from flask_ngrok import run_with_ngrok

app_n = Flask(__name__)
run_with_ngrok(app_n)

@app_n.route('/', methods=['GET'])
def api():
    d = {}
    data = str(request.args['message'])
    answer = str(ask(data))
    d['answer'] = answer
    return d

if __name__ == '__main__':
    app_n.run()


