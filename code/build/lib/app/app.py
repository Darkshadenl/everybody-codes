from flask import Flask
from io import StringIO
import csv
from flask import make_response
from app.main import handleNameArg


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/csv", methods=['GET'])
def csv():
    pass

if __name__ == "__main__":
    app.run()