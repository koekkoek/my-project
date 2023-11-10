from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello World! This is awesome. Even after an update3.</p>"


@app.route("/contact")
def contact():
    return "<p>Would you like to contact me? E-mail: info@my-project.nl.</p>"
