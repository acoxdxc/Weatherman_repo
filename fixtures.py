from flask import Flask, json, jsonify
app= Flask(__name__)


fixture = '''[{"id": 1, "name": "London", "weather": "rainy"}, {"id": 2, "name": "New York", "weather": "sunny"}, {"id": 3, "name": "paris", "weather": "snowy"}, {"id": 4, "name": "madrid", "weather": "sunny"}, {"id": 5, "name": "berlin", "weather": "rainy"}]'''

Weather_object= json.loads(fixture)

@app.route("/")
def index():
    return "weather API"

@app.route("/weather")
def weather():
    return jsonify(Weather_object)

if __name__ == '__main__':
    app.run(port = 5000)
