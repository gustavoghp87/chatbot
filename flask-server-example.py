from flask import Flask, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import pandas as pd
import sys


app = Flask(__name__)


@app.route('/chat', methods=['GET'])
def ping():
    return 'Hello world'
    # return jsonify({"response": "hello world"})

@app.route('/users')
def userHandler():
    return jsonify({'users': [{"user":"user1"}, {"user":"user2"} ]})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6000, debug=False)

# acceso desde el exterior:   flask run --host=0.0.0.0    después de cargar la variable de entorno para flask   set ...