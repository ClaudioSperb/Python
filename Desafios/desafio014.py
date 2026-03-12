grauCelsios = float(input('Digite a temperatura de sua Cidade: ºC >>>'))
fahrenheit = (grauCelsios * 1.8) + 32
kelvin = grauCelsios + 273.15
print('-' * 15)
print(f'A sua cidade esta com {grauCelsios}ºC, convertendo para Fahrenheit fica {fahrenheit}ºF')
print('-' * 15)
print(f'Em Kelvin sua temperatura é de {kelvin}K')

