from time import sleep
from colorama import Fore, Back, Style, init
init(autoreset=True)
vel = float(input('Digite sua velocidade atual: '))
multa = (vel - 80) * 7
print(f'Sua velocidade é de {vel:.1f}Km/h')
print('RADAR - Analisando sua Velocidade...')
sleep(2)
if vel >= 80:
    print(f'Você esta a {vel}Km/h e foi {Fore.LIGHTRED_EX}MULTADO !!!')
    print(f'O valor da multa é de R${multa:.2f} reais.')
else:
    print(f'{Fore.LIGHTGREEN_EX}Você esta a {vel}Km/h - BOA VIAGEM !!!!')
