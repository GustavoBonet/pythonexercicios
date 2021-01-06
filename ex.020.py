import random
a = input('aluno:')
b = input('aluno:')
c = input('aluno:')
d = input('aluno:')
l = [a,b,c,d]
random.shuffle(l)
print(f' A sequência de apresentação é \n {l}')
