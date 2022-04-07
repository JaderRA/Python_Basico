#nomes = ['Jader', 'Joao', 'Leticia', 'Nathan']
#palavra='jader foquinha'
#for i in palavra:
    #print(i)
#i=0
# i+=1 corresponde a i = i+1, incremento: i++
#numero=0
#while True:
 #   print(numero)
  #  if numero == 20:
   #     break;
    #numero +=1

#Exercício proposto:
print('Convidados da festa')
total = input('\nQuantos convidados terá a festa? ')
lista=[]
i=0
for i in range(int(total)):
    pos=input('\nEscreva o nome do convidado '+ str(i+1) +': ')
    lista.append(pos)
    i+=1

print('A festa possui ', total, 'convidados.')

for x in lista:
    print(x)
