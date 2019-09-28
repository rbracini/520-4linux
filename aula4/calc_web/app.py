from flask import Flask, render_template, request
from calculadora import Calculadora

app = Flask(__name__)
calculadora = Calculadora()

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    num1 = int(request.form['nm1'])
    num2 = int(request.form['nm2'])
    
    return str(calculadora.somar(num1, num2))

if __name__ == "__main__":
    app.run(debug=True)