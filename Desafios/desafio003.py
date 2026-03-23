from colorama import Fore, Back, Style
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
soma = num1 + num2
print(f'A soma de {Fore.LIGHTBLUE_EX}{num1}{Fore.RESET} e {Fore.LIGHTCYAN_EX}{num2}{Fore.RESET} é {Fore.LIGHTGREEN_EX}{soma}{Fore.RESET}')
