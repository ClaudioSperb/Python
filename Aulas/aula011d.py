from colorama import init, Fore, Back, Style
#INICIALIZANDO O COLORAMA
init()
num = int(input('Digite um numero: '))
if num % 2 == 0:
    print(f'O numero digitado é {Fore.LIGHTGREEN_EX}{num}{Style.RESET_ALL} e ele é {Fore.LIGHTGREEN_EX}PAR{Style.RESET_ALL}')
else:
    print(f'O numero digitado é {Fore.RED}{num}{Style.RESET_ALL} e ele é {Fore.LIGHTRED_EX}ÍMPAR{Style.RESET_ALL}')
