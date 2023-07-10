from flask import Flask, request, jsonify
from flask_cors import CORS

from app import App


flask_app = Flask(__name__)
CORS(flask_app)
lang_app = App()


@flask_app.route('/language_detector/language', methods=['PUT', 'GET'])
def detect_language_endpoint():
    method = request.method

    match method:
        case 'PUT':
            text_input = request.get_json()['text_input']
            lang_app.compute_language(text_input)
            return jsonify({'message': 'Success'}), 200

        case 'GET':
            language_code = lang_app.get_language()
            return {'language_code': language_code}


if __name__ == '__main__':
    flask_app.run()
