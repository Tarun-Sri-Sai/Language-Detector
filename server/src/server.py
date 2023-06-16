import flask
import ngram_char as nc
import flask_cors as fc


app = flask.Flask(__name__)
fc.CORS(app)


@app.route('/detect-language', methods=['GET'])
def detect_language_endpoint():
    input_text = flask.request.args.get('input_text', '')
    language_code = nc.detect_language(input_text)
    return {'language_code': language_code}


if __name__ == '__main__':
    app.run()
