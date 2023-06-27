import flask
from app import App
import flask_cors as fc


flask_app = flask.Flask(__name__)
fc.CORS(flask_app)
lang_app = App()


@flask_app.route('/detect-language', methods=['GET'])
def detect_language_endpoint():
    input_text = flask.request.args.get('input_text', '')
    language_code = lang_app.detect(input_text)
    return {'language_code': language_code}


if __name__ == '__main__':
    flask_app.run()
