n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o último número: '))

if n1 > n2 and n1 > n3:
    print(f'O valor maior é {n1}')
elif n2 > n3 and n2 > n1:
    print(f'O numero maior é {n2}')
else:
    print(f'O numero maior é {n3}')
print(15 *'-')

if n1 < n2 and n1 < n3:
    print(f'O número menor é {n1}')
elif n2 < n3 and n2 < n1:
    print(f'O número menor é {n2}')
else:
    print(f'O número menor é {n3}')
print(15 * '-')
print('FIM DO PROGRAMA !!')