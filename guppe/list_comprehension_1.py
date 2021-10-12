"""
List Comprehension
- Utilizando List comprehension podemos gerar novas listas com dados processados a partir de outro iterável

# Sintaxe da List Comprehension

[ dado for dado in iteravel]
"""
# Exemplos

numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros]  # lembra comando CROSS APPLY em T-SQL
print(res)

"""
Para entender melhor o que está acontecendo, devemos dividir a expressão em duas partes:
- for numero in numeros
- numero * 10 

res = [numero / 2 for numero in numeros]
print(res)


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]
print(res)

# list comprehension vs loop

# loop
numeros_dobrados = []

for numero in [1, 2, 3, 4, 5]:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados)

# List comprehension
print([numero * 2 for numero in [1, 2, 3, 4, 5]])
"""

# outros exemplos

# 1

nome = 'Geek University'
print([letra.upper() for letra in nome])

# 2
amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([amigo.title() for amigo in amigos])


# ou
def caixa_alta(nome):
    return nome.replace(nome[0], nome[0].upper())

print([caixa_alta(amigo) for amigo in amigos])


# 3
print([numero * 3 for numero in range(1, 10)])

# 4
print([bool(valor) for valor in [0, [], '', True, 1, 3, 14]])

# 5
print([str(numero) for numero in [1, 2, 3, 4, 5]])
