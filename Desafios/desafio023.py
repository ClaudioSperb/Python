numeroQualquer = int(input('Digite um numero qualquer: '))
u = numeroQualquer // 1 % 10
d = numeroQualquer // 10 % 10
c = numeroQualquer // 100 % 10
m = numeroQualquer // 1000 % 10

print(f'Analisando o numero {numeroQualquer} >>> ')
print(f'unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')



