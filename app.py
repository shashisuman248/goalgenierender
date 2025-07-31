from flask import Flask, request, jsonify, render_template
from logic import get_recommendation

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    recommendation = get_recommendation(data)
    return jsonify(recommendation)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
