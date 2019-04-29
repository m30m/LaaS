from flask import Flask, send_from_directory
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('form.html')


@app.route('/download', methods=['GET'])
def download():
    pass


@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=False, host='0.0.0.0')
