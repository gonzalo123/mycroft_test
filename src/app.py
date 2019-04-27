from flask import Flask, jsonify
import os
from dotenv import load_dotenv
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(dotenv_path="{}/.env".format(current_dir))

app = Flask(__name__)


@app.route('/check/<key>', methods=['GET'])
def check(key):
    file_name = './db/{}.json'.format(key)
    if os.path.isfile(file_name):
        with open(file_name) as json_data:
            d = json.load(json_data)
            json_data.close()
        return jsonify({
            'text': d['description'],
            'name': d['name']
        })
    else:
        return jsonify({'text': "No conozco la fruta {}. ¿Que te has creido que soy? Esto es un prototipo. ¿Seguro que no quieres decier Mango?".format(key)})


if __name__ == "__main__":
    app.run(host='0.0.0.0')
