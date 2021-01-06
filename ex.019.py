import random
a = input('primeiro aluno:')
b = input('segundo aluno:')
c = input('terceiro aluno:')
d = input('quarto aluno')
lista = [a,b,c,d]
print(f'O aluno escolhido foi {random.choice(lista)}')

