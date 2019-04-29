import json
import tempfile

from flask import Flask, send_from_directory, send_file
from flask import render_template
from flask import request
from generators import digikala, snapp, tap30, cafe

import pandas as pd

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('form.html')


@app.route('/download', methods=['GET'])
def download():
    db = request.args.get('db')
    count = min(int(request.args.get('count')), 1000)
    format = request.args.get('format')

    db_dict = {'digikala': digikala,
               'snapp': snapp,
               'tap30': tap30,
               'cafe': cafe}
    results = []
    for i in range(count):
        results.append(db_dict[db]())

    handle, filepath = tempfile.mkstemp()
    if format == 'csv':
        df = pd.DataFrame.from_dict(results)
        df.to_csv(filepath, index=False)
        return send_file(filepath, attachment_filename=db + '_leakage.csv', as_attachment=True)
    else:
        with open(filepath, 'w') as fw:
            fw.write(json.dumps(results, indent=2))
        return send_file(filepath, attachment_filename=db + '_leakage.json', as_attachment=True)


@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=False, host='0.0.0.0')
