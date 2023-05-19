import datetime as dt

from flask import Flask, abort

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/datetime/")
@app.route("/datetime/<timezone>")
def datetime(timezone=0):
    try:
        timezone = int(timezone)
        app.logger.info("Reached convert timezone in type data int.")
    except Exception as e:
        abort(406, "You enter wrong type of timezone. Please enter information in digital type.")

    if 12 >= timezone >= -12:
        current_time = dt.datetime.now()
        finally_current_time = current_time + dt.timedelta(hours=int(timezone))
        return f"<h3>Time: {finally_current_time.strftime('%H:%M:%S')}. Timezone GMT {timezone}.</h3>"
    else:
        abort(406, "You enter wrong timezone, more than 12 or less than -12.")


@app.route("/datetime")
def datetime_def():
    return f"You must use only numbers that more than 12 and less than -12." \
           f"Right format:" \
           f".../datetime/-2" \
            f".../datetime/4" \
            f"Wrong format:" \
            f".../datetime/43" \
            f".../datetime/sdasda"


if __name__ == "__main__":
    import logging
    app.logger.setLevel(logging.DEBUG)
    app.run(host="127.0.0.1", port=5000, debug=True)
