import requests
import random

url = 'http://127.0.0.1:8000/api/'
for i in range(99):
    myobj = {
        'w_temp': f'{random.randint(25, 36)}',
        'w_humidity': f'{random.randint(10, 100)}',
        'l_humidity_1': f'{random.randint(10, 100)}',
        'l_humidity_2': f'{random.randint(10, 100)}'
    }

    headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json'
    }

    x = requests.post(url, data=myobj)

print(x.text)
print(x.status_code)
