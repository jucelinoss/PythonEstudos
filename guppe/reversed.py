""""
Reversed

- n]ão confundir com a função reverse() das listas
A função reverse funciona apenas em listas, enquanto a função reversed funciona com qualquer iterável
A função reversed retorna uma iterável chamado List Reverse Iterator
"""
# Exemplos
lista = [1, 2, 3, 4, 5]
res = reversed(lista)

print(res)
print(type(res))

# Podemos converter o elemento retornado para lista, Tupla ou Conjunto
print(list(reversed(lista)))

print(tuple(reversed(lista)))

print(set(reversed(lista))) # set não preserva a ordem dos elementos nem repetição do dado

# iterar sobre o reversed
for letra in reversed('Geek University'):
    print(letra, end='')

print('\n')
# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Geek University'))))

# slice de strings
print('Geek University'[::-1])

# Podemos utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)


print('\n')
for n in range(9, -1, -1):
    print(n)