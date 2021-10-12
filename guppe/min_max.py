"""
Min e Max
max() -> retorna o maior valor em um iterável ou o maior de dois ou mais elementos


# Exemplos
lista = [1, 8, 44, 99, 34, 129]
print(max(lista))   # 129

tupla = (1, 8, 44, 99, 34, 129)
print(max(tupla))   # 129

conjunto = {1, 8, 44, 99, 34, 129}
print(max(conjunto))   # 129

dicionario = {'a': 1, 'b': 8, 'c': 44, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario))   # f

dicionario = {'a': 1, 'b': 8, 'c': 44, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario.values()))   # 129

print(max(3, 34)) #34

# Faca um programa que receba dois valores do usuári e mostre o maior
val1 = int(input("Informe o primeiro valor"))
val2 = int(input("Informe o segundo valor"))
print(max(val1, val2))

print(max(3.145, 5.789))

print(max('Geek University'))

min() - retorna o menotr valor em um iterável ou o menor de dois ou mais elementos
# Exemplos
lista = [1, 8, 44, 99, 34, 129]
print(min(lista))   # 129

tupla = (1, 8, 44, 99, 34, 129)
print(min(tupla))   # 129

conjunto = {1, 8, 44, 99, 34, 129}
print(min(conjunto))   # 129

dicionario = {'a': 1, 'b': 8, 'c': 44, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario))   # f

dicionario = {'a': 1, 'b': 8, 'c': 44, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario.values()))   # 129

print(min(3, 34)) #34

# Faca um programa que receba dois valores do usuári e mostre o maior
val1 = int(input("Informe o primeiro valor"))
val2 = int(input("Informe o segundo valor"))
print(min(val1, val2))

print(min(3.145, 5.789))

print(min('Geek University'))
"""

# Outros Exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
print(max(nomes))   # texto em ordem alfabética
print(min(nomes))


print(max(nomes, key = lambda nome: len(nome)))     # Ollivander
print(min(nomes, key = lambda nome: len(nome)))     # Tim


musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too young to die", "tocou": 32}
]
print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# Musicas mais e menos tocadas
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# Como encontrar a musica mais e menos tocada sem usar max min e lambdas
max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] > max:
        print(musica['titulo'])

min = 99999
for musica in musicas:
    if musica['tocou'] > max:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])

min = 99999
for musica in musicas:
    if musica['tocou'] > max:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])
