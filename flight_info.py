from flask import Flask, json, jsonify
app= Flask(__name__)

info = '''[{"destination": "London", "code": "LON1"}, {"destination": "New York", "code": "NY1"}, {"destination": "Paris", "code": "PAR1"}, {"destination": "Madrid", "code" : "MAD1"}, {"destination": "Berlin", "code": "BER1"}]'''

info_object=json.loads(info)

@app.route("/")
def index():
    return "Flight codes API"

@app.route("/info")
def info():
    return jsonify(info_object)


if __name__ == "main":
    app.run(port = 4500)