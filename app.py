from flask import Flask, jsonify

app = Flask(__name__)
# this is the added line

@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify({'message': 'Hello from Flask!'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
