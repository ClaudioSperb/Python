n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
soma = n1 + n2
subt = n1 - n2
mult = n1 * n2
divnor = n1 / n2
divint = n1 // n2
pot = n1**n2
restdiv = n1 % n2

print(f'O valor da soma entre eles é {n1+n2}')
print(f'O valor da subtração é {n1 - n2}, da multiplicação é {mult}, da divisão é {divnor:.3f}')
print(f'O valor da divisão inteira é {divint}, da potencia é {pot} e do resto da divisão é {restdiv}')
