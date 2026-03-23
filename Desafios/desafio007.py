from colorama import Fore

nomeAluno = str(input('Nome do Aluno: ')).upper().strip()
notaAluno = float(input('Digite a nota da sua primeira prova: '))
notaAluno2 =float(input('Digite a nota da sua segunda prova: '))
mediaAluno = (notaAluno + notaAluno2) / 2
if mediaAluno >= 6:
    print(f'Olá {nomeAluno}, seja bem Vindo !!!')
    print(f'Sua média foi de {Fore.LIGHTGREEN_EX}{mediaAluno}{Fore.RESET}')
    print(f'Parabens você foi {Fore.LIGHTGREEN_EX} APROVADO {Fore.RESET} !!!')
else:
    print(f'Ola {nomeAluno}, sua média foi de {Fore.LIGHTRED_EX}{mediaAluno}{Fore.RESET}')
    print(f'Infelizmente voce esta {Fore.LIGHTRED_EX} REPROVADO !!!{Fore.RESET}')

#print(f'Seja bem vindo {nomeAluno}, você tirou na sua primeira prova {notaAluno} e na segunda prova {notaAluno2}, então a sua média ficou {(notaAluno + notaAluno2) / 2 }')