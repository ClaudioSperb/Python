from random import shuffle

n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do segundo aluno: '))
n3 = str(input('Nome do terceiro aluno: '))
n4 = str(input('nome do quarto aluno: '))
listaAlunos = [n1, n2, n3, n4]
shuffle(listaAlunos)
print('A ordem de apresentação ficou: >>>')
print(listaAlunos)