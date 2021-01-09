a = int(input('Digite o número:'))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
op = int(input('Sua opção:'))
if op == 1:
    print(f'{a} convertido para binário fica {bin(a)[2:]}')
elif op == 2:
    print(f'{a} convertido para OCTAL fica {oct(a)[2:]}')
elif op == 3:
    print(f'{a} convertido para HEXADECIMAL fica {hex(a)[2:]}')
else:
    print('Opção inválida tente novamente.')

# ler numero inteiro , escolher base de conversao
# binario , octal ou hexadecimal
# mostrar como fica em cada
