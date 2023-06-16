from flask import Flask, request
from ngram_char import detect_language
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/detect-language', methods=['GET'])
def detect_language_endpoint():
    input_text = request.args.get('input_text', '')
    language_code = detect_language(input_text)
    return {'language_code': language_code}


if __name__ == '__main__':
    app.run()
