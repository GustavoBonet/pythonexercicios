prova1 = float(input('Primeira nota:'))
prova2 = float(input('Segunda nota:'))
media = (prova1 + prova2) / 2
if media <= 4.9:
    print('Você foi \033[1:30:41mREPROVADO.\033[m')
elif 5 <= media <= 6.9:
    print('Você está de \033[1:30:43mRECUPERAÇÃO.\033[m')
elif media <= 10:
    print('Você foi \033[1:30:42mAPROVADO.\033[m')
else:
    print('Tente novamente')
