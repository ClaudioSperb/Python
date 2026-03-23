from time import sleep
from colorama import Fore

retaUm = int(input('Digite um número qualquer inteiro: '))
retaDois = int(input('Digite mais um número inteiro qualquer: '))
retaTres = int(input('Digite o último número inteiro qualquer: '))
print('Verificando as medidas digitadas ...')
sleep(2)
print(f'Você digitou - {retaUm}, {retaDois} e {retaTres}')
if retaUm + retaDois > retaTres and retaUm + retaTres > retaDois and retaDois + retaTres > retaUm:
    print(f'{Fore.LIGHTGREEN_EX}Com as medidas passadas , é possivel fazer um Triangulo')
else:
    print(f'{Fore.LIGHTRED_EX}Infelizmente nao da para formar um Triângulo')