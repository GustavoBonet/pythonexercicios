from datetime import date
atual = date.today().year
dn = int(input('Digite o seu ano de nascimento:'))
idade = atual - dn
if idade == 18:
    print('Você está na idade para se alistar.')
elif idade >= 19:
    passou = idade - 18
    print(f'Você já passou {passou} anos do alistamento.')
elif idade <= 17:
    falta = 18 - idade
    print(f'Você ainda tem {falta} para se alistar..')
else:
    print('Mulher não precisa se alistar.')
