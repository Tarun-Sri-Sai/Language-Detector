from flask import Flask, request, jsonify
from flask_cors import CORS

from app import App


flask_app = Flask(__name__)
CORS(flask_app)
lang_app = App()


@flask_app.route('/language_detector/language', methods=['POST'])
def detect_language_endpoint():
    text_input = request.json['text_input']
    lang_app.compute_language(text_input)
    language_code = lang_app.get_language()
    return {'language_code': language_code}


if __name__ == '__main__':
    flask_app.run()
