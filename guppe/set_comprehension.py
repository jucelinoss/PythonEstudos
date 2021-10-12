"""
Set comprehension

"""

# Exemplos

numeros = {num for num in range(1, 7)}
print(numeros)

# Outro exemplo
numeros = {x ** 2 for x in range(10)}
print(numeros)

# geração de dicionário
numeros = {x: x ** 2 for x in range(10)}
print(numeros)

letras = {letra for letra in 'Geek University'} # conjuntos não repetem e não têm ordenação
print(letras)
