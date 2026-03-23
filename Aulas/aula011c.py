#CRIANDO UM ROOT DE CORES COM OBJETO
coresSistema = {'verde': '\033[1;32m', 'vermelho': '\033[1;31m'}
nomeCliente = str(input('Qual seu nome Completo: '))

print(f'Ola {coresSistema['verde']}{nomeCliente}')