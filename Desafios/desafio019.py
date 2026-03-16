import random
aluno01 = str(input('Digite o nome do aluno: '))
aluno02 = str(input('Digite o nome do outro aluno: '))
aluno03 = str(input('Digite o nome do outro aluno: '))
aluno04 = str(input('Digite o nome do último aluno: '))
listaSorteio = [aluno01, aluno02, aluno03, aluno04]
sorteioFinal = random.choice(listaSorteio)
print(f'O aluno sorteado para apagar o quadro foi {sorteioFinal}')
