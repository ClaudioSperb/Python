dias = int(input('Quantos dias voce esta com o veiculo? '))
valorDiaria = dias * 60
km = float(input('Quantos Km você rodou? '))
valorkmRodado = km * 0.15
valorTotal = valorDiaria + valorkmRodado
print(f'Você rodou {km}km e ficou {dias} dias com o veículo, o valor total ficou R${valorTotal:.2f} reais.')
