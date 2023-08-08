from flask import Flask, request, jsonify
from app import ask


app = Flask(__name__)


@app.route('/algo', methods=['GET'])
def api():
    d = {}
    data = str(request.args['query'])
    answer = str(ask(data))
    d['answer'] = answer
    return d

if __name__ == '__main__':
    app.run(debug=True)


