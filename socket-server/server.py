from flask import Flask, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import pandas as pd
import sys


app = Flask(__name__)

bot = ChatBot(
    'MaslaChat',  
    logic_adapters = ['chatterbot.logic.BestMatch']
)
trainer = ListTrainer(bot)

data = pd.read_excel('frases.xlsx')

list = []

for i in data.index:
    try:
        clave = str(data['clave'][i])
        frase = str(data['frase'][i])
        print(i)
        if clave!='nan':
            list.append(clave)
            list.append(clave)
            print(clave)
        list.append(frase)
        list.append(frase)
        print(frase)
    except:
        print("error")

    if i > 360:
        break


trainer.train(list)

#trainer = ChatterBotCorpusTrainer(bot)
# trainer.train("chatterbot.corpus.spanish")
# trainer.train("chatterbot.corpus.spanish.greetings")
# trainer.train("chatterbot.corpus.spanish.conversations")
# trainer.train("chatterbot.corpus.spanish.dinero")
# trainer.train("chatterbot.corpus.spanish.IA")
# trainer.train("chatterbot.corpus.spanish.emociones")
# trainer.train("chatterbot.corpus.spanish.perfilbot")
# trainer.train("chatterbot.corpus.spanish.psicologia")
# trainer.train("chatterbot.corpus.spanish.trivia")


print('\n')



@app.route('/chat', methods=['GET'])
def ping():

    # name = input("Ingresa tu nombre: ")
    name = 'nombre'

    print('\n')

    while True:
        # request = input(name.upper() + ':  ')
        request = ''
        for arg in sys.argv:
            request += str(arg) + ' '
        if request=='Bye' or request =='bye':
            print('MASLACHAT: Bye')
            break
        else:
            response=bot.get_response(request)
            print('MASLACHAT: ', response, '\n')


    return 'Hello world'
    # return jsonify({"response": "hello world"})

@app.route('/users')
def userHandler():
    return jsonify({'users': [{"user":"user1"}, {"user":"user2"} ]})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6000, debug=False)
