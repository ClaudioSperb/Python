nomeUsuario = str(input('Digite seu nome: ')).strip().title()
print(f'Olá {nomeUsuario}')
distancia = float(input('Digite a Km desejada para sua viagem: '))
valorNormal = distancia * 0.5
valorPromoc = distancia * 0.45
print(f'Certo {nomeUsuario}, a distancia escolhida foi de {distancia:.2f}km')
print('CALCULANDO o valor total ...')
if distancia <= 200:
    print(f'O valor da viagem ficou em R${valorNormal:.2f} reais')
else:
    print(f'O valor total da sua viagem ficou R${valorPromoc:.2f} reais.')
print(20 * '-')
print('Obrigado por usar nosso SISTEMA !!! ')