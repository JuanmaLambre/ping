from flask import Flask

# dummy commit

app = Flask(__name__)


@app.route('/')
def ping():
    return "Hello world :)"

@app.route('/ping')
def ping():
    return "Pong!"


def main():
    app.run(host='0.0.0.0', port=4804)


if __name__ == "__main__":
    main()
