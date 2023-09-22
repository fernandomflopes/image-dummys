from flask import Flask
from flask import send_file

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<button onclick='location.href=\"/rand\"'>Get Random Image</button>"


@app.route("/rand")
def get_file():
    import os
    import random

    f_names = os.listdir("media")

    rand_file = "media/" + f_names[random.randint(0, len(f_names) - 1)]
    
    return send_file(rand_file, as_attachment=True)
