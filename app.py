#coding: utf-8

from flask import Flask, jsonify
from services.firebaseAccess import FireBase
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify(af.getAdm()), 200

# **************************************** Init ****************************************
if __name__ == "__main__":
    af = FireBase()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)