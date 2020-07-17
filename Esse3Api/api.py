import requests
import json

class Carriera:
    def __init__(self, data):
        self.corso_di_studi = data['cdsDes']
        self.matricola = data['matricola']
        self.matId = data['matId']
        self.motStastuDes = data['motStastuDes']
        self.staMatDes = data['staMatDes']
        self.staStuDes = data['staStuDes']
        self.stuId = data['stuId']

class Student:
    def __init__(self, data):
        self.username = data['credentials']['user']
        self.CF = data['user']['codFis']
        self.name = data['user']['firstName'].title()
        self.surname = data['user']['lastName'].title()
        self.group = data['user']['grpDes']
        self.id = data['user']['id']
        self.persId = data['user']['persId']
        self.carriera_completa = [ Carriera(x) for x in data['user']['trattiCarriera'] ]
        self.carriera = 0

    def seleziona_carriera(self, index):
        self.carriera = index

    def carriera(self):
        return self.carriera_completa[self.carriera]

class Esse3API:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.auth = (username, password)
        auth = self.session.get(self.base_url + 'login')
        response = json.loads(auth.text)
        if auth.status_code != 200 or ('statusCode' in response and response['statusCode'] == 401):
            raise Exception('Invalid credentials')
        if response['user']['grpDes'] != 'Studenti':
            raise Exception('Only studens are supported right now')
        self.user = Student(response)

