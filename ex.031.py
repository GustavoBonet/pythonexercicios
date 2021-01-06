dis = float(input('Distância em km :'))
if dis < 200:
    pre = dis * 0.50
else:
    pre = dis * 0.45
print(f'O preço da passagem será de R${pre:.2f}')


