# Primeros pasos con Flask Socket IO desde cero, comunicación Full Duplex Cliente y Servidor #1


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_World():
    return "Olá MUndo!"

if __name__ == '__main__':
    app.run()