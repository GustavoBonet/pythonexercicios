a = str (input('Digite uma frase:')).upper().strip()
print(f' A letra A aparece {a.count("A")} na frase.')
print(f'A letra A aparece na posição {a.find("A")+1}')
print (f' A última letra A aparece na posição {a.rfind("A")+1}')
