import requests
import time
import datetime
import json

while True:
    req = requests.get('https://economia.awesomeapi.com.br/json/all')
    dic = json.loads(req.text)
    print('### Cotação ###  ', datetime.datetime.now())
    print('Dólar: ', dic['USD']['high'], 'reais')
    print('Euro: ', dic['EUR']['high'], 'reais')
    print('Bitcoin: ', dic['BTC']['high'], 'reais')
    time.sleep(3)