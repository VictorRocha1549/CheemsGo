from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify ({"success":True, "message":"Hello World"}),200

if __name__ == '__main__':
    app.run(port=5001)
