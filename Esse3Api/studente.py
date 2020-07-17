import json
import requests

from Esse3Api.carriera import Carriera

class Student:
    def __init__(self, data, full_career):
        self.__username = data['credentials']['user']
        self.CF = data['user']['codFis']
        self.name = data['user']['firstName'].title()
        self.surname = data['user']['lastName'].title()
        self.group = data['user']['grpDes']
        self.id = data['user']['id']
        self.persId = data['user']['persId']
        self.carriera_completa = [ Carriera(x, full_career) for x in data['user']['trattiCarriera'] ]
        self.carriera_index = 0

    def seleziona_carriera(self, index):
        if index < 0 or index > len(self.carriera_completa):
            raise Exception('Career index out of range')
        self.carriera_index = index

    def carriera(self):
        return self.carriera_completa[self.carriera_index]

    def carriera_completa(self):
        return self.carriera_completa

    def libretto(self, session):
        return self.carriera_completa[self.carriera_index].libretto(session)

    def tasse(self, session):
        return self.carriera_completa[self.carriera_index].tasse(session)
