endpoints = {
    'POLIBA': {
        'url': 'https://poliba.esse3.cineca.it/e3rest/api/',
        'description': 'Politecnico di Bari'
    },
    'UNIBAS': {
        'url': 'https://unibas.esse3.cineca.it/e3rest/api/',
        'description': 'Università degli Studi della Basilicata'
    },
    'UNIBA': {
        'url': 'https://www.studenti.ict.uniba.it/e3rest/api/',
        'description': 'Università degli Studi di Bari Aldo Moro'
    },
    'UNIBG': {
        'url': 'https://sportello.unibg.it/e3rest/api/',
        'description': 'Università degli Studi di Bergamo'
    },
    'UNIBS': {
        'url': 'https://esse3.unibs.it/e3rest/api/',
        'description': 'Università degli Studi di Brescia'
    },
    'UNICAL': {
        'url': 'https://unical.esse3.cineca.it/e3rest/api/',
        'description': 'Università della Calabria'
    },
    'UNICAMPANIA': {
        'url': 'https://esse3.cressi.unicampania.it/e3rest/api/',
        'description': 'Università degli Studi della Campania Luigi Vanvitelli'
    },
    'UNICAMPUS': {
        'url': 'https://didattica.unicampus.it/e3rest/api/',
        'description': 'Università Campus Bio-Medico di Roma'
    },
    'UNICAM': {
        'url': 'https://didattica.unicam.it/e3rest/api/',
        'description': 'Università di Camerino'
    },
    'UNICA': {
        'url': 'https://unica.esse3.cineca.it/e3rest/api/',
        'description': 'Università degli Studi di Cagliari'
    },
    'UNICH': {
        'url': 'https://unich.esse3.cineca.it/e3rest/api/',
        'description': 'Università degli Studi G. D\'Annunzio Chieti Pescara'
    },
    'UNIFI': {
        'url': 'https://studenti.unifi.it/e3rest/api/',
        'description': 'Università degli Studi di Firenze'
    },
    'UNIMARCONI': {
        'url': 'https://unimarconi.esse3.cineca.it/e3rest/api/',
        'description': 'Università degli Studi Guglielmo Marconi'
    },
    'UNIME': {
        'url': 'https://unime.esse3.cineca.it/e3rest/api/',
        'description': 'Università degli Studi di Messina'
    },
    'UNIMIB': {
        'url': 'https://s3w.si.unimib.it/e3rest/api/',
        'description': 'Università degli Studi di Milano-Bicocca'
    },
    'UNIMORE': {
        'url': 'https://www.esse3.unimore.it/e3rest/api/',
        'description': 'Università degli Studi di Modena e Reggio Emilia'
    },
    'UNINSUBRIA': {
        'url': 'https://uninsubria.esse3.cineca.it/e3rest/api/',
        'description': 'Università degli Studi dell\'Insubria'
    },
    'UNIPG': {
        'url': 'https://unipg.esse3.cineca.it/e3rest/api/',
        'description': 'Università degli Studi di Perugia'
    },
    'UNIPI': {
        'url': 'https://www.studenti.unipi.it/e3rest/api/',
        'description': 'Università di Pisa'
    },
    'UNIPR': {
        'url': 'https://unipr.esse3.cineca.it/e3rest/api/',
        'description': 'Università di Parma'
    },
    'UNIPV': {
        'url': 'https://studentionline.unipv.it/e3rest/api/',
        'description': 'Università degli Studi di Pavia'
    },
    'UNIRSM': {
        'url': 'https://unirsm.esse3.cineca.it/e3rest/api/',
        'description': 'Università degli Studi della Repubblica di San Marino'
    },
    'UNISANNIO': {
        'url': 'https://unisannio.esse3.cineca.it/e3rest/api/',
        'description': 'Università degli Studi del Sannio'
    },
    'UNITN': {
        'url': 'https://www.esse3.unitn.it/e3rest/api/',
        'description': 'Università degli Studi di Trento'
    },
    'UNITO': {
        'url': 'https://esse3.unito.it/e3rest/api/',
        'description': 'Università di Torino'
    },
    'UNITS': {
        'url': 'https://esse3.units.it/e3rest/api/',
        'description': 'Università degli Studi di Trieste'
    },
    'UNIUD': {
        'url': 'https://uniud.esse3.cineca.it/e3rest/api/',
        'description': 'Università degli Studi di Udine'
    },
    'UNIURB': {
        'url': 'https://uniurb.esse3.cineca.it/e3rest/api/',
        'description': 'Università degli Studi di Urbino Carlo Bo'
    },
    'UNIVAQ': {
        'url': 'https://univaq.esse3.cineca.it/e3rest/api/',
        'description': 'Università degli Studi dell\'Aquila'
    },
    'UNIVE': {
        'url': 'https://esse3.unive.it/e3rest/api/',
        'description': 'Università Ca\' Foscari Venezia'
    },
    'UNIVPM': {
        'url': 'https://univpm.esse3.cineca.it/e3rest/api/',
        'description': 'Università Politecnica delle Marche'
    }
}

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def prompt():
    url_map = [ uni for uni in endpoints ]
    for index, value in enumerate(url_map):
        print('%d) %s' % (index + 1, endpoints[value]['description']))
    valid = False
    while not valid:
        key = input('Seleziona università: ')
        if RepresentsInt(key) and int(key) > 0 and int(key) <= len(url_map):
            valid = True
    return endpoints[url_map[int(key) - 1]]['url']


