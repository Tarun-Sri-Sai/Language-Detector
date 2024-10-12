from flask import Flask, request, jsonify
from flask_cors import CORS

from language import Language


server = Flask(__name__)
CORS(server)
language = Language()


@server.route('/language_detector/language', methods=['POST'])
def detect_language_endpoint():
    text_input = request.json['text_input']
    language_code = language.compute_language(text_input)
    return {'language_code': language_code}


if __name__ == '__main__':
    server.run(host='0.0.0.0')
