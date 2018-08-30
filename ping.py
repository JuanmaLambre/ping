from flask import Flask
import RPi.GPIO as GPIO


OUT_PINS = [24]
app = Flask(__name__)


@app.route('/')
def ping():
    return "Ping pong!"

@app.route('/led/<ledNo>/on')
def ledOn(ledNo):
    GPIO.output(int(ledNo), GPIO.HIGH)
    return "LED " + ledNo + " is on"

@app.route('/led/<ledNo>/off')
def ledOff(ledNo):
    GPIO.output(int(ledNo), GPIO.LOW)
    return "LED " + ledNo + " is off"


def setup():
    GPIO.setmode(GPIO.BCM)
    for pin in OUT_PINS:
        GPIO.setup(pin, GPIO.OUT)


def main():
    setup()
    app.run(host='0.0.0.0', port=4804)


if __name__ == "__main__":
    main()
