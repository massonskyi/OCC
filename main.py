import subprocess
from flask import Flask, render_template, request, jsonify
from utils.execute import execute_code, translate_text

app = Flask(__name__)

USING_LANGUAGE = ['python', 'c', 'cpp', 'js', 'cs', 'ruby', 'go']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/translate', methods=['POST'])
def run_translate():
    before_lang: str = request.json['before']
    after_lang: str = request.json['after']
    text: str = request.json['text']
    output = translate_text(
        {'text': text, 'before': before_lang, 'after': after_lang})
    result = {
        'output': output
    }
    return jsonify(result)


@app.route('/runcode', methods=['POST'])
def run_code():
    code = request.json['code']
    language = request.json['language']
    if language in USING_LANGUAGE:
        try:
            output, error = execute_code({'lang': language, 'code': code})
        except subprocess.CalledProcessError as e:
            output = ''
            error = str(e)
        except Exception as e:
            output = ''
            error = str(e)

        result = {
            'output': output,
            'error': error
        }
    else:
        result = {
            'output': '',
            'error': 'Unsupported language'
        }
    return jsonify(result)


if __name__ == '__main__':
    app.run()
