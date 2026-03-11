valorSalario = float(input('Digite o valor do seu salario: R$'))
aumentoSalario = valorSalario * (15 / 100)
print(f'Atualmente seu salário é de R${valorSalario:.2f} \ncom o aumento de 15% seu salário passou para \nR${valorSalario + aumentoSalario:.2f} Reais')
print('-' * 25)
salarioAumento = valorSalario + aumentoSalario

dicidio2025 = valorSalario + (valorSalario * 7.5 / 100)
print(f'O valor de R${aumentoSalario + valorSalario} reais com o reajuste do Dicidio de 7.5% fica {aumentoSalario + dicidio2025:.2f} reais')