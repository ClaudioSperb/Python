#MANIPULANDO TEXTOS EM PYTHON
#        0123456789...........
from itertools import count

texto = 'Curso em Vídeo Python'
texto2 = '     Python é legal     '
print(texto[0:5])
print(texto[0::2])
print(texto[9:])
print(len(texto))#Aqui pega o comprimento da string
print(texto.count('e'))
print(texto.find('hon'))
print(texto.find('Android')) #Aqui da -1, pois essa string nao existe
print('Curso' in texto) # TRUE
print(texto.upper())
print(texto.lower())
print(texto.capitalize())
print(texto.title())
print(texto2.strip())
print(texto2.rstrip())
print(texto2.lstrip())
print(texto.replace('Curso', 'Modulo'))
