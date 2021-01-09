from datetime import date
atual = date.today().year
anonasc = int(input('Digite seu ano de nascimento:'))
idade = atual - anonasc
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('Classificação:\033[:30:45mMIRIM \033[m')
elif idade <= 14:
    print('Classificação:\033[:30:45mINFANTIL\033[m')
elif idade <= 19:
    print('Classificação:\033[:30:45mJUNIOR\033[m')
elif idade <= 25:
    print('Classificação:\033[:30:45mSÊNIOR\033[m')
else:
    print('Classificação:\033[:30:45mMASTER\033[m')
