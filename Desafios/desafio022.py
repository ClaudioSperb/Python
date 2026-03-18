nome = str(input('Digite seu nome completo: ')).strip()
nomelimpo = "".join(nome.split())
primeiroNome = nome.split()
print(f'Seu nome completo é {nome}')
print(f'Seu nome com todas as letras em maiusculas: {nome.upper()}')
print(f'Seu nome com todas as letras em minusculas: {nome.lower()}')
print(f'Seu nome sem espaços fica {nomelimpo} e contem {len(nomelimpo)} letras')
print(f'Seu primeiro nome é {primeiroNome[0]} e tem {len(primeiroNome[0])} letras')


