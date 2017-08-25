#coding: utf-8

from firebase import firebase

class FireBase(object):

    def __init__(self):
        self.adm = "olá"

    def getAdm(self):
        fire = firebase.FirebaseApplication('https://login-94c17.firebaseio.com/', None)

        # segundo argumento passa o filho.
        resp = fire.get('/usuarios', None)

        #j = {'id': 5}
        #result = fire.patch('/usuarios/amanda/', j)
        return resp
