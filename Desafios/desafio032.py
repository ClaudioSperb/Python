from datetime import date
nome = str(input('Digite seu nome: ')).strip().title()
print(f'Ola {nome}! ')
anoNascimento = int(input('Digite o ano do seu nascimento: '))
print(f'Olá, {nome}, o ano do seu nascimento é {anoNascimento}')
if anoNascimento % 4 == 0 and anoNascimento % 100 != 0 or anoNascimento % 400 == 0:
    print(f'O ano {anoNascimento} é um ano BISSEXTO')
else:
    print(f'O ano {anoNascimento} não é BISSEXTO')

#PARA PEGAR A DATA ATUAL
anoAtual = date.today().year
print(f'O ano atual é {anoAtual}')