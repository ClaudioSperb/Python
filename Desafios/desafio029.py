vel = float(input('Digite sua velocidade atual: '))
multa = (vel - 80) * 7
print(f'Sua velocidade é de {vel:.1f}Km/h')
print('RADAR - Analisando sua Velocidade...')
if vel >= 80:
    print(f'Você esta a {vel}Km/h e foi MULTADO !!!')
    print(f'O valor da multa é de R${multa:.2f} reais.')
else:
    print(f'Você esta a {vel}Km/h - BOA VIAGEM !!!!')
