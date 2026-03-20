salario = float(input('Digite seu salário atual: R$'))
aumentoDez = salario * (10 / 100) + salario
aumentoquinze = salario * (15 / 100) + salario
#print(f'R${aumentoDez:.2f}, R${aumentoquinze:.2f}')
print(f'Seu salário atual é R${salario:.2f} reais. Verificando seu Aumento >>> ')
if salario <= 1250.00:
    print(f'Você ganhou um aumento de 15% e seu salário agora é R${aumentoquinze:.2f} reais')
else:
    print(f'Você ganhou um aumento de 10% e se salário agora é R${aumentoDez:.2f} reais')
print('FIM DO PROGRAMA')