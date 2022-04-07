import requests

header={'User-agent': 'Windows 12', 'Referer': 'https://google.com'}
bolinho={'Ultima visita': '10-10-2020'}
dados={'username': 'fodao', 'password': 'bilau'}
texto=None
try:
    requi=requests.post('https://putsreq.com/',
                        headers=header, cookies=bolinho, data=dados)
    texto=requi.text
except Exception as e:
    print('Cagou', e)
print(texto)
