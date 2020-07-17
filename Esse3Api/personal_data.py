class Address:
    def __init__(self, data, suffix):
        self.cap = data['cap' + suffix]
        self.comune = data['comu' + suffix + 'Des']
        self.comune_sigla = data['comu' + suffix + 'Sigla']
        self.nazione = data['nazi' + suffix + 'Des']
        self.via = data['via' + suffix]
        self.civico = data['numCiv' + suffix]
        self.telefono = data['tel' + suffix]

class PersonalData:
    def __init__(self, data):
        self.name = data['nome'].title()
        self.surname = data['cognome'].title()
        self.codice_fiscale = data['codFis']
        self.data_nascita = data['dataNascita']
        self.comune_nascita = data['comuNascDes']
        self.nazione_nascita = data['naziNascDes']
        self.email = data['email']
        self.email_ateneo = data['emailAte']
        self.userId = data['userId']
        self.sesso = data['sesso']
        self.domicilio = Address(data, 'Dom')
        self.residenza = Address(data, 'Res')
