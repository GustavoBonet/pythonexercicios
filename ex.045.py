import random
from time import sleep
print(' [ 1 ] PEDRA \n [ 2 ] PAPEL \n [ 3 ] TESOURA')
jogada = int(input('Sua jogada é:'))
print('....')
sleep(2)
lista = [1, 2, 3]
computador = random.choice(lista)
if jogada == 1 and computador == 2:
    print('Computador jogou Papel \n Computador venceu')
elif jogada == 1 and computador == 3:
    print('Computador jogou tesoura \n Jogador venceu')
elif jogada == 2 and computador == 1:
    print('Computador jogou pedra \n Jogador venceu')
elif jogada == 2 and computador == 3:
    print('Computador jogou tesoura \n Computador venceu')
elif jogada == 3 and computador == 1:
    print('Computador jogou pedra \n Computador venceu')
elif jogada == 3 and computador == 2:
    print('Computador jogou papel \n Jogador venceu')
