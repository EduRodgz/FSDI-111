from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def name():
    data = {
        "first_name": "Eduardo",
        "last_name": "Rodriguez",
        "hobby": "Gym"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
