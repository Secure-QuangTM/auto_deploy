from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World - by QUANGTM - test!</p>"

if __name__ == '__main__':
    app.run(debug=True)