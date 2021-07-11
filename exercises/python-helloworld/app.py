from flask import Flask
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def healthcheck():
    response = app.response_class(
        response = json.dumps({"result": "OK - healthy"}),
        status = 200,
        mimetype = 'application.json',
    )
    return response

@app.route("/metrics")
def metrics():
    context = {
        "data": {
            "UserCount": 14,
            "UserCountActive": 23
            }
    }
    return context

if __name__ == "__main__":
    app.run(host='127.0.0.1')
