# coding: utf-8

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from services.firebaseAccess import FireBase
import os
from services.cross import crossdomain

app = Flask(__name__)
CORS(app)

# Rota padrão
@app.route("/")
def hello_world():
    return jsonify(af.getAdm()), 200


@app.route("/getusuario/<nome>", methods=['GET'])
def getusuario(nome):

    return jsonify(af.getUsuario(nome)), 200


@app.route("/doLogin", methods=['POST'])
@cross_origin()
def doLogin():
    print 'VAIIIIIIIIIIIIIIIIIII'
    print request.data
    return 'ok', 200


# **************************************** Init ****************************************
if __name__ == "__main__":
    af = FireBase()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)