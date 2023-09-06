from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye():
    return "Bye!"

@app.route("/<name>")
def greet(name):
    return f"hello there {name}"

if __name__ == "__main__":
    app.run(debug=True)
