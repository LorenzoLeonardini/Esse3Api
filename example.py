import Esse3Api.api as esse3
import Esse3Api.endpoint
from getpass import getpass

import os

if __name__ == '__main__':
    if not os.path.isfile('credentials'):
        user = input('Username: ')
        password = getpass('Password: ')
        url = Esse3Api.endpoint.prompt()
    else:
        file = open('credentials', 'r')
        url = file.readline().strip()
        user = file.readline().strip()
        password = file.readline().strip()
        file.close()

    api = esse3.Esse3API(url, user, password)
    user = api.user()
    print('USER')
    print('\tName surname: %s %s' % (user.name, user.surname))
    print('\tCF: %s' % user.CF)
    print('\tGroup: %s' % user.group)
    carriera = api.carriera()
    print('CARRIERA')
    print('\tCDS: %s' % carriera.corso_di_studi)
    print('\tMatricola: %s (%s)' % (carriera.matricola, carriera.matId))
    print('\tStatus: %s %s %s' % (carriera.motStastuDes, carriera.staMatDes, carriera.staStuDes))
    print('\tAnno Accademico: %s' % (carriera.anno_accademico))
    print('\tAnno Corso: %s' % (carriera.anno_corso))
    print('\tDate:')
    print('\t\tImm: %s' % (carriera.dataImm))
    print('\t\tIns: %s' % (carriera.dataIns))
    print('\t\tIscr: %s' % (carriera.dataIscr))
    print('\t\tMod: %s' % (carriera.dataMod))
    personal = api.personal_data()
    print('PERSONAL DATA:')
    print('\tNome: %s %s' % (personal.name, personal.surname))
    print('\tCF: %s' % personal.codice_fiscale)
    print('\tData di nascita: %s' % personal.data_nascita)
    print('\tComune di nascita: %s' % personal.comune_nascita)
    print('\tNazione di nascita: %s' % personal.nazione_nascita)
    print('\tEmail: %s' % personal.email)
    print('\tEmail Ateneo: %s' % personal.email_ateneo)
    print('\tSesso: %s' % personal.sesso)
    print('\tDomicilio:')
    print('\t\t%s %s, %s (%s) %s, %s\n\t\t%s' % (personal.domicilio.via, personal.domicilio.civico, personal.domicilio.comune, personal.domicilio.comune_sigla, personal.domicilio.cap, personal.domicilio.nazione, personal.domicilio.telefono))
    print('\tResidenza:')
    print('\t\t%s %s, %s (%s) %s, %s\n\t\t%s' % (personal.residenza.via, personal.residenza.civico, personal.residenza.comune, personal.residenza.comune_sigla, personal.residenza.cap, personal.residenza.nazione, personal.residenza.telefono))
    libretto = api.libretto()
    print('LIBRETTO:')
    prev_anno = -1
    for anno in libretto.esami_per_anno:
        if len(anno) == 0:
            continue
        if anno[0].anno_corso != prev_anno:
            print('\tEsami del %d anno' % anno[0].anno_corso)
            prev_anno = anno[0].anno_corso
        for corso in anno:
            print('\t\t%s (%s)' % (corso.nome, corso.codice))
            print('\t\t\tAnno frequenza: %s' % (corso.anno_frequenza))
            print('\t\t\tCFU: %s' % (corso.cfu))
            print('\t\t\tTipo esame: %s' % (corso.tipo_esame))
            print('\t\t\tStato: %s' % (corso.stato))
            print('\t\t\tAnno superamento: %s' % (corso.anno_superamento))
            print('\t\t\tData esame: %s' % (corso.data_esame))
            print('\t\t\tVoto: %s%s' % (corso.voto, 'L' if corso.lode else ''))
    tasse = api.tasse()
    print("TASSE")
    print('\tSemaforo: %s' % tasse.semaforo)
    print('\tImporto dovuto: %s' % tasse.importo_dovuto)
