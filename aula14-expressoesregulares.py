import re
import requests

req=requests.get('https://www.asics.com.br/atendimento-email')

padrao=re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', req.text)    #raw string (carcteres "sem poderes")

if padrao:
    print(padrao)
else:
    print('Padrão não encontrado')