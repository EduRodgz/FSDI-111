from flask import Flask

app = Flask(__name__)



@app.get("/")
def index():
    me = {
        "first_name": "Eduardo",
        "last_name": "Rodriguez",
        "hobbies": "Gym",
        "is_active": True
    }
    return me