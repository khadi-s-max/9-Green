from flask import Flask, jsonify 

app = Flask(__name__)

@app.route('/api/v1/users', methods=['GET'])
def get_users():
    return jsonify({"users": ["Alice", "Bob", "Charlie"]})

if __name__ == '__main__':
    app.run(debug=True)



""" new """