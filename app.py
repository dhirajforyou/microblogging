from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, world!"


@app.route('/user/<name>')
def user(name):
    return f"<h1>Hello, {name}</h1>"


def main():
    app.run(host="0.0.0.0", port=6001, debug=True)


if __name__ == "__main__":
    main()
