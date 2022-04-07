import time

def abre_arquivo():
    try:
        arquivo=open('arquiv.txt')
        return True
    except  Exception as errado:
        print("Fudeu:\n", errado)
        return False

while not abre_arquivo():
    print('Trying to open file: ')
    time.sleep(5)

print('Sucess')


