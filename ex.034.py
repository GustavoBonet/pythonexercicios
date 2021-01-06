a = float (input('Digite o salário R$'))
b = a*10/100
c = a*15/100
if a > 1250:
    print(f'O seu novo salário será de R${a+b :.2f}')
else:
    print(f'O seu novo salário será de R${a+c:.2f}')
