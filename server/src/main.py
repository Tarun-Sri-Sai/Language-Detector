from flask import Flask, request
from .language import Language


server = Flask(__name__)
language = Language()


@server.route('/api/language', methods=['GET'])
def detect_language_endpoint():
    text_input = request.json['text_input']
    language_code = language.compute_language(text_input)
    return {'language_code': language_code}
