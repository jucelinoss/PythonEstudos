"""
Sorted
Obs.: Não confundir com a função sort(), que funciona somente com listas
Sorted() pode ser utulizado com qualquer iterável
Serve para ordenar elementos
o comando sorted() sempre retorna uma lista ordenada com os elementos iterável passado como parâmetro

# Exemplo

numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros)) # não altera a ordem do iterável; retorna iterável ordenado, sem alterá-lo

numeros = [6, 1, 8, 2]
# Adicionando parãmetros ao sorted()
print(sorted(numeros))

print(sorted(numeros, reverse=True)) # ordena em ordem descendente

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "Carla", "tweets": ["Eu amo meu gato"]},
    {"username": "Jeff", "tweets": []},
    {"username": "Bob123", "tweets": [], "cor":"amarelo"},
    {"username": "Doggo", "tweets": ["Eu gosto de cachorros", "vou sair hoje"]},
    {"username": "Gal", "tweets": [], "cor":"preto", "Música":"rock"}
]

print(usuarios)
# print(sorted(usuarios)) # sorted não consegue ordenar dicionários sem informar chave
print(sorted(usuarios, key=lambda usuario: usuario["username"])) # ordenação por username
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"]))) # ordenação pela qtd de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"]), reverse=True))   # ordenação pela qtd de tweets (maior ao menor)


"""

# Ultimo exemplo

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too young to die", "tocou": 32}
]

# Ordena da menos Tocada para a mais Tocada
print(sorted(musicas, key=lambda musica: musica["tocou"]))

# Ordena da Mais Tocada para a menos Tocada
print(sorted(musicas, key=lambda musica: musica["tocou"], reverse=True))


