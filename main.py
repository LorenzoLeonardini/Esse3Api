import Esse3Api.api as esse3
import Esse3Api.endpoint

import os

if not os.path.isfile('credentials'):
    user = input('Username: ')
    password = input('Password: ')
    url = Esse3Api.endpoint.prompt()
else:
    file = open('credentials', 'r')
    url = file.readline().strip()
    user = file.readline().strip()
    password = file.readline().strip()
    file.close()

esse3 = esse3.Esse3API(url, user, password)
