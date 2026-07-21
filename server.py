from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "OpenOSINT API работает"


@app.route("/api/search", methods=["POST"])
def search():

    data = request.json

    return jsonify({
        "type": data.get("type"),
        "query": data.get("query"),
        "status": "API подключен"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
