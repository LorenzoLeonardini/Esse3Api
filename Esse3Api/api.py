import json
import requests

from Esse3Api.carriera import Carriera
from Esse3Api.libretto import Libretto, Esame
from Esse3Api.personal_data import PersonalData, Address
from Esse3Api.studente import Student
from Esse3Api.tasse import Tasse

class Esse3API:
    def __init__(self, base_url, username, password):
        self.__base_url = base_url
        self.__session = requests.Session()
        self.__session.auth = (username, password)
        auth = self.__session.get(self.__base_url + 'login')
        response = json.loads(auth.text)
        if auth.status_code != 200 or ('statusCode' in response and response['statusCode'] == 401):
            raise Exception('Invalid credentials')
        if response['user']['grpDes'] != 'Studenti':
            raise Exception('Only studens are supported right now')
        full_career = json.loads(self.__session.get(self.__base_url + 'anagrafica-service-v2/carriere').text)
        self.__user = Student(response, full_career)
        self.__personal_data = False

    def seleziona_carriera(self, index):
        self.__user.seleziona_carriera(index)

    def carriera(self):
        return self.__user.carriera()

    def carriera_completa(self):
        return self.__user.carriera_completa()

    def user(self):
        return self.__user

    def personal_data(self):
        if not self.__personal_data:
            data = json.loads(self.__session.get(self.__base_url + 'anagrafica-service-v2/persone').text)
            self.__personal = PersonalData(data[0])
        return self.__personal

    def libretto(self):
        return self.__user.libretto((self.__session, self.__base_url))

    def tasse(self):
        return self.__user.tasse((self.__session, self.__base_url))

    def propic(self):
        return self.__user.propic((self.__session, self.__base_url))
