larg = float (input('Digite a largura da sua parede: '))
alt = float (input('Agora, me passe a altura da parede: '))
areaTotal = larg * alt
lataTinta = (areaTotal * 1) / 2
print(f'As medidas da sua parede é {larg} x {alt}, a area total é de {areaTotal} m² quadrados')
print(f'Você precisa comprar {lataTinta:.2f}l de tinta')