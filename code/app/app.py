from flask import Flask
from io import StringIO
import csv
from flask import make_response


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/csv", methods=['GET'])
def csv():
    return 'hi'

if __name__ == "__main__":
    app.run()