from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello world :D"

@app.route('/ping')
def ping():
    return "Pong!"


def main():
    app.run(host='0.0.0.0', port=4804)


if __name__ == "__main__":
    main()
