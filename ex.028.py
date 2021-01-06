from random import randint
print('-=-' * 20)
pc = randint (0,10)
print('Vou pensar em um número entre 0 e 10')
player = int(input('Em que número pensei?'))

if pc == player:
    print(f'{pc} Parabéns! Você acertou! =)')
else:
    print(f'Eu Ganhei! haha, mais sorte na próxima, pensei no {pc} e não no {player}')
print('-=-'*20)

#JOGO DE ADIVINHAÇAO