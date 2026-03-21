vel = float(input('Digite sua velocidade atual: '))
multa = (vel - 80) * 7
print(f'Sua velocidade é de {vel:.1f}Km/h')
print('RADAR - Analisando sua Velocidade...')
if vel > 80:
    print(f'Você esta a {vel}Km/h e foi \033[1;97;41m  MULTADO !!!\033[m')
    print(f'\033[1;97;43mO valor da multa é de R${multa:.2f} reais.\033[m')
else:
    print(f'\033[1;32mVocê esta a {vel}Km/h - BOA VIAGEM !!!!')
