from flask import Flask
import json
import logging
app = Flask(__name__)

@app.route("/")
def hello():
    # log line
    app.logger.info("Main request successfull.")
    return "Hello World!"

@app.route("/status")
def healthcheck():
    response = app.response_class(
        response = json.dumps({"result": "OK - healthy"}),
        status = 200,
        mimetype = 'application.json',
    )
    # log line
    app.logger.info("Status request successfull.")
    return response

@app.route("/metrics")
def metrics():
    context = {
        "data": {
            "UserCount": 14,
            "UserCountActive": 23
            }
    }
    # log line
    app.logger.info("Metrics request successfull.")
    return context

if __name__ == "__main__":

    # stream logs to app.log file
    logging.basicConfig(filename='app.log', level=logging.DEBUG)

    app.run(host='127.0.0.1')
