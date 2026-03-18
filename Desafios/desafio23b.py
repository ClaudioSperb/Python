#USANDO O .zfill()

num = input('Digite um número de 0 a 9999: ').zfill(4)
print(f'Analisando o numero {num}...')
print(f'Unidade: {num[3]}')
print(f'Dezena: {num[2]}')
print(f'Centena: {num[1]}')
print(f'Milhar: {num[0]}')

