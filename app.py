from flask import Flask, render_template, request, jsonify
from logic import get_recommendation

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def recommend():
    try:
        data = request.get_json()
        recommendation = get_recommendation(data)
        return jsonify(recommendation)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
