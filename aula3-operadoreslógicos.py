print('Cadastro no Exército')

idade=input('\nEscreva sua idade: ')
peso=input('\nEscreva seu peso: ')
altura=input('\nEscreva sua altura: ')

if idade>='18' and peso>='60' and altura>='1,70':
    print("\nVocê está apto para entrar no Exército!")
else:
    print('\nVocê não está apto para entrar no Exército')