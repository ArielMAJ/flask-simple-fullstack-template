"""App's entrypoint file."""

from datetime import datetime
from random import random

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return process_form()
    return render_template("index.html", utc_dt=get_utc_now())


def process_form():
    number1 = process_number(request.form.get("number1"))
    number2 = process_number(request.form.get("number2"))
    number3 = process_number(request.form.get("number3"))

    return render_template(
        "index.html", utc_dt=get_utc_now(), numbers=[number1, number2, number3]
    )


def get_utc_now():
    return datetime.utcnow().strftime("%H:%M:%S, %d/%m/%Y")


def process_number(number):
    return round(2 * random() * int(number) ** 2, 2)
