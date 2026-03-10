valorItem = float (input('Digite o valor de item desejado: '))
desconto = valorItem * (5 / 100)
print(f'O item tem o valor de R${valorItem:.2f}, com 5% de desconto, seu item fica R${valorItem - desconto:.2f} reais')
