preco = float(input('Preço total: R$'))
print(' [ 1 ] DINHEIRO OU CHEQUE 10% OFF \n [ 2 ] DÉBITO 5% OFF \n [ 3 ] ATÉ 2X NO CRÉDITO')
print('[ 4 ] 3X A 12X NO CRÉDITO 20% DE JUROS')
opcao = int(input('Qual sua opção:'))
if opcao == 1:
    print(f'Sua compra de {preco:.2f} vai custar {preco - (preco * 10/100):.2f}')
elif opcao == 2:
    print(f'Sua compra de {preco:.2f} vai custar {preco - (preco * 5/100):.2f}')
elif opcao == 3:
    parcelas1 = int(input('Quantas parcelas [ 1 ] ou [ 2 ]:'))
    print(f'Sua compra custa {preco:.2f}')
    if parcelas1 == 2:
        print(f'Parcelada em 2x fica {preco/2:.2f}')
elif opcao == 4:
    parcelas2 = int(input('Quantas parcelas:'))
    preco_com_juros = preco + (preco * 20/100)
    print(f'Sua compra custa {preco:.2f} vai custar {preco_com_juros:.2f}')
    print(f'E parcelada em {parcelas2}x fica {preco_com_juros / parcelas2:.2f}')
else:
    print('Opção inválida. tente novamente!')
