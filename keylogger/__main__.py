from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def hello_world():
    code = request.args.get("code")
    print(code)
    return "OK"

if __name__ == "__main__":
    app.run(host="127.0.0.1")
