from flask import Flask, request, jsonify
from flask_cors import CORS
from ..mcq_generator.mcq_generator import generate_mcqs
app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
    r'/*': {
        'origins': '*'
    }
})
@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/gen', methods=['POST'])
def generate():
    text = request.json['text']
    response = jsonify(generate_mcqs(text))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)
