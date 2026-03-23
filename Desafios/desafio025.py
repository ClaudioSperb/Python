from time import sleep

nomeCompleto = str(input('Digite seu nome completo: ')).strip().upper()
validandoNome = 'SILVA' in nomeCompleto
print(f'Seu nome completo é {nomeCompleto} >>>> ')
print(f'Validando se o nome possui "SILVA" >>> ......')
sleep(2)
print('.........')
print(f'Validação concluída: {validandoNome}')
