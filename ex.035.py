r1 = int(input('primeira reta:'))
r2 = int(input('segunda reta:'))
r3 = int(input('terceira reta:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print ('Podem formar um triângulo!')
else:
    print('Não podem formar um triângulo!')
