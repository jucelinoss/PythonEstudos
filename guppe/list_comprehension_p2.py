"""
List Comprehension

Podemos adicionar estruturas condicionais lógicas as nossas List Comprehension
"""

# Exemplos

# 1


numeros = [1, 2, 3, 4, 5, 6]
pares = [numero for numero in numeros if numero % 2 == 0]

impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# refatoração
# Qualquer numero par módulo de 2 é o 0 e 0 em Python é False. Not False = True
pares = [numeros for numero in numeros if not numero % 2]

# Qualquer numero impart módulo de 2 é 1, e em python é True
impares = [numeros for numero in numeros if numero % 2]

print(pares)
print(impares)

# 2
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)

