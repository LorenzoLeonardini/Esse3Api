class Esame:
    def __init__(self, data):
        self.anno_frequenza = data['aaFreqId']
        self.nome = data['adDes']
        self.codice = data['adCod']
        self.anno_corso = data['annoCorso']
        self.cfu = data['peso']
        self.tipo_esame = data['tipoEsaDes']
        self.stato = data['statoDes']
        self.anno_superamento = data['esito']['aaSupId']
        self.data_esame = data['esito']['dataEsa']
        self.voto = data['esito']['voto']
        self.lode = data['esito']['lodeFlg']

class Libretto:
    def __init__(self, data):
        self.esami = [None] * len(data)
        self.esami_per_anno = [ [] for i in range(10) ]
        index = 0
        for entry in data:
            exam = Esame(entry)
            self.esami[index] = exam
            index += 1
            anno = exam.anno_corso
            self.esami_per_anno[anno - 1].append(exam)
