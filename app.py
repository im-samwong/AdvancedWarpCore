from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/add', methods=['POST'])
def add_five():
    data = request.json
    number = data['number']
    result = number + 5
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)