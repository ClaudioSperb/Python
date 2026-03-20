import random
from time import sleep
num = int(input('Digite um numero de 0 a 5: '))
print('PROCESSANDO')
sleep(3)
numMaquina = random.randint(0, 5)
print(f'O numero escolhido pela Máquina foi >>> {numMaquina}')
sleep(2)
if num == numMaquina:
    print('Muito bem !!!, você advinhou o número')
else:
    print('Ah que pena, a Máquina ganhou de Você !!')
print('<<< FIM DE JOGO >>>')