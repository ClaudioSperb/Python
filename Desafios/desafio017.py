from math import hypot, sin, cos
catOposto = float(input('Digite o valor do cateto oposto: '))
catAdjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot(catOposto, catAdjacente)
print(f'Se o cateto oposto é {catOposto} e o catetto adjacente é {catAdjacente} então o valor da Hipotenusa é {hipotenusa:.2f}')