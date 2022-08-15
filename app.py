from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'hello world'

@app.route('/about', methods=['GET'])
def about():
    return jsonify({"hello": "world"})

if __name__ == '__main__':
    app.run(debug=True)
