

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Dünya!</p>"

@app.route("/merhaba")
def merhaba():
    return "<p>Hello!</p>"

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=22222)