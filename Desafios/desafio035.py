retaUm = int(input('Digite um número qualquer inteiro: '))
retaDois = int(input('Digite mais um número inteiro qualquer: '))
retaTres = int(input('Digite o último número inteiro qualquer: '))
print('Verificando as medidas digitadas ...')
print(f'Você digitou - {retaUm}, {retaDois} e {retaTres}')
if retaUm + retaDois > retaTres and retaUm + retaTres > retaDois and retaDois + retaTres > retaUm:
    print(f'Com as medidas passadas , é possivel fazer um Triangulo')
else:
    print('Infelizmente nao da para formar um Triângulo')