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
    info = None
    if os.path.isfile(file_name):
        with open(file_name) as json_data:
            d = json.load(json_data)
            json_data.close()
        if d['description_en'] != '':
            info = jsonify({
                'text': d['description_en'],
                'name': d['name_en']
            })

    if info == None:
        info = jsonify({'text': "I don't know the fruit {}. Who the *#!# do you think I am? This is just a pilot. Maybe you meant Mango?".format(key)})

    return info


if __name__ == "__main__":
    app.run(host='0.0.0.0')
