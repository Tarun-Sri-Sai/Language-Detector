from app import App

import flask as fl
import flask_cors as fc


flask_app = fl.Flask(__name__)
fc.CORS(flask_app)
lang_app = App()


@flask_app.route('/detect-language', methods=['POST', 'GET', 'DELETE'])
def detect_language_endpoint():
    method = fl.request.method

    match method:
        case 'POST':
            text_input = fl.request.get_json()['text_input']
            lang_app.compute_language(text_input)
            return fl.jsonify({'message': 'Success'}), 200

        case 'GET':
            language_code = lang_app.get_language()
            return {'language_code': language_code}

        case 'DELETE':
            lang_app.clear_language()
            return fl.jsonify({'message': 'Success'}), 200


if __name__ == '__main__':
    flask_app.run()
