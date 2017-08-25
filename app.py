#coding: utf-8

from flask import Flask, jsonify
from services.firebaseAccess import FireBase

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify(af.getAdm()), 200

# **************************************** Init ****************************************
if __name__ == "__main__":
    af = FireBase()
    app.run(host='0.0.0.0', port=8989, threaded=True, debug=True)