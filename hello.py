from flask import Flask, render_template, url_for
from datetime import datetime

app = Flask(__name__)


# filtros personalizados
@app.add_template_filter
def today(date):
    return date.strftime("%d/%m/%Y")


# funcion personalizada
@app.add_template_global  # agregado global
def repeat(s, n):
    return s * n


@app.route("/")
@app.route("/index")
def index():
    # print(url_for("code", code='print("Hola")'))
    print()
    print()
    name = "Nicolongoso"
    friends = ["Pata", "Peta", "Pita", "Pota"]
    date = datetime.now()
    return render_template(
        "index.html",
        name=name,
        friends=friends,
        date=date,
    )


@app.route("/hello")
@app.route("/hello/<name>")
@app.route("/hello/<name>/<int:age>/<email>")
def hello(name=None, age=None, email=None):
    my_data = {
        "name": name,
        "age": age,
        "email": email,
    }
    return render_template("hello.html", data=my_data)
