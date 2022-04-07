import requests
import json

req=None

def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?apikey={key}='  + titulo + '&type=movie')
        dic = json.loads(req.text)
        return dic
    except:
        print('Erro na conexão')
        return None

def print_details(filme):
    print('Titulo: ', filme['Title'])
    print('Ano: ', filme['Year'])
    print('Lançamento: ', filme['Released'])
    print('Gênero: ', filme['Genre'])
    print('Diretor: ', filme['Director'])
    print('Elenco: ', filme['Actors'])
    print('Nota: ', filme['imdbRating'])
    print('Duração: ', filme['Runtime'])
    print('Prêmios: ', filme['Awards'])
    print('Postêr: ', filme['Poster'])
    print('')

sair=False
while not sair:
    op =input('Escreva o nome de um filme ou SAIR para fechar: ')
    if op == 'SAIR':
        sair=True
        print('Saindo...')
    else:
        filme=requisicao(op)
        if filme['Response'] == False:
            print('Filme não encontrado')
        else:
            print_details(filme)
