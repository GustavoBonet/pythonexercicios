valorcasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
tempofinanciamento = float(input('Quantos anos de financiamento:'))

anos_em_meses = tempofinanciamento * 12
prestacao = valorcasa / anos_em_meses
parte = salario * 30 / 100

print(
    f'Para pagar uma casa de R${valorcasa:.2f} em {tempofinanciamento:.0f} anos a prestação será de R${prestacao:.2f}')

if prestacao <= parte:
    print('Empréstimo APROVADO !')
else:
    print('Empréstimo NEGADO !')

# exercicio de emprestimo usando if e else
# parte significa 30% do salario do comprador
# pois apenas é aceito o emprestimo se a prestacao for menor que 30% do salario do comprador
