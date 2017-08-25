#coding: utf-8

from firebase import firebase
from models.usuario import Usuario
import json

class FireBase(object):

    def __init__(self):
        self.adm = "olá"
        self.usuario = Usuario(0, '', '', '', '')

    def getAdm(self):
        fire = firebase.FirebaseApplication('https://login-94c17.firebaseio.com', None)

        # segundo argumento passa o filho.
        resp = fire.get('/usuarios', None)

        #j = {'id': 5}
        #result = fire.patch('/usuarios/amanda/', j)
        return resp

    def __getUserFireBase(self, nome):
        fire = firebase.FirebaseApplication('https://login-94c17.firebaseio.com', None)
        resp = fire.get('/usuarios', nome)
        return resp


    # Retorna os dados do usuário cujo nome foi passado.
    def getUsuario(self, nome):
        res = self.__getUserFireBase(nome)
        return res

    def login(self, data):
        nome = data['nome']
        dados = self.__getUserFireBase(nome)

        if dados != None:
            if dados['senha'] != data['senha']:
                return None
            else:
                dados

        return dados