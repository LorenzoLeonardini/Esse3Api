import json
import requests

from Esse3Api.libretto import Libretto
from Esse3Api.tasse import Tasse

class Carriera:
    def __init__(self, data, full_career):
        self.corso_di_studi = data['cdsDes']
        self.matricola = data['matricola']
        self.matId = data['matId']
        self.motStastuDes = data['motStastuDes']
        self.staMatDes = data['staMatDes']
        self.staStuDes = data['staStuDes']
        self.stuId = data['stuId']

        for career in full_career:
            if career['stuId'] != self.stuId:
                continue
            self.anno_accademico = career['aaDes']
            self.anno_corso = career['annoCorso']
            self.dataImm = career['dataImm']
            self.dataIns = career['dataIns']
            self.dataIscr = career['dataIscr']
            self.dataMod = career['dataMod']
            break

        self.libretto_loaded = False
        self.tasse_loaded = False

    def libretto(self, session):
        if not self.libretto_loaded:
            data = session[0].get(session[1] + 'libretto-service-v2/libretti/' + str(self.matId) + '/righe')
            data = json.loads(data.text)
            self.libretto_obj = Libretto(data)
            self.libretto_loaded = True
        return self.libretto_obj

    def tasse(self, session):
        if not self.tasse_loaded:
            data = session[0].get(session[1] + 'tasse-service-v1/semaforo/' + str(self.stuId))
            data = json.loads(data.text)
            self.tasse_obj = Tasse(data)
            self.tasse_loaded = True
        return self.tasse_obj
