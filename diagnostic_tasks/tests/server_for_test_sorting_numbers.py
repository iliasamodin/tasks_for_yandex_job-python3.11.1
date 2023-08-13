"""
The server for processing the get-request of the first test 
for the "sorting numbers" task.
"""

from flask import Flask, request, make_response, abort
import json

SECRET_KEY = "}GE2{H>C1#OD9HK2ZK.e1t`&K3qfu`FhK'vUyKa+eSX&d<U:=$]a8,.("
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
def send_numbers():
    if request.method == "GET" and \
    request.args.get("a") == "2" and request.args.get("b") == "4":
        resulting_numbers = json.dumps(
            [8, 6, -2, 2, 4, 17, 256, 1024, -17, -19]
        )
        server_response = make_response(resulting_numbers)
        server_response.headers["Content-Type"] = "text/json"
        return server_response
    else:
        abort(404) 


if __name__ == "__main__":
    app.run(port=7777, debug=True)