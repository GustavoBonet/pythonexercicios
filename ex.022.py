a = input('digite seu nome completo:')
print(f' Analisando seu nome ... \n Em maiúsculo fica {a.upper()} \n Em minúsculo fica {a.lower()}')
print (' Tem {} letras'.format (len(a) - a.count(' ')))
ab = a.split()
print(f' E o seu primeiro nome tem {len(ab[0])} letras')






#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.