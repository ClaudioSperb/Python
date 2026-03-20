import random
num = int(input('Digite um numero de 0 a 5: '))
numMaquina = random.randint(0, 5)
print(f'O numero escolhido pela Máquina foi >>> {numMaquina}')
if num == numMaquina:
    print('Muito bem !!!, você advinhou o número')
else:
    print('Ah que pena, a Máquina ganhou de Você !!')
print('<<< FIM DE JOGO >>>')