a = int(input('Digite um valor:'))
b = int(input('Digite um valor:'))
c = int(input('Digite um valor:'))

#menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print (f' O maior é {maior} e o menor é {menor}.')
