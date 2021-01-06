#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

a = str(input('Digite seu nome:')).strip()
b = a.split()
print('Prazer em te conhecer =)')
print(f'Seu primeiro nome é {b[0]} \n E seu último nome é {a[-1]}')

# ESSE PROGRAMA NÃO ESTÁ FUNCIONANDO , NÃO ENTENDI OQUE OCORREU