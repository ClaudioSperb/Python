larg = float (input('Digite a largura da sua parede: '))
alt = float (input('Agora, me passe a altura da parede: '))
areaTotal = larg * alt
lataTinta = (areaTotal * 1) / 2
galaoTinta = (lataTinta / 3.6)
print('-' * 30)
print(f'As medidas da sua parede é {larg} x {alt}, a area total é de {areaTotal} m² quadrados')
print(f'Você precisa comprar {lataTinta:.2f} l de tinta')
print(f'Você vai precisar de {galaoTinta:.2f} latas de 3.6l')
print('-' * 30)
print('Lembrando que para ter um bom desempenho, aplique de 2 a 3 Demãos !!!')