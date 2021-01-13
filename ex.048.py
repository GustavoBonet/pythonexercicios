soma = 0
contador = 0
# do 1 ate 501 pulando 2, para saber os n° ímpares (1 3 5 7 ....)
for x in range(1, 501, 2):
    if x % 3 == 0:
        contador = contador + 1    # contador = contador + 1 é igual ao de baixo só escreve diferente
        soma = soma + x                  # soma += i  ==  soma = soma + i
print(f' A soma de todos os {contador} valores é {soma}')
