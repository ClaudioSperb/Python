import math
catOposto = int(input('Digite o valor do cateto oposto: '))
catAdjacente = int(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(catOposto, catAdjacente)
print(f'Se o cateto oposto é {catOposto} e o catetto adjacente é {catAdjacente} então o valor da Hipotenusa é {hipotenusa:.2f}')