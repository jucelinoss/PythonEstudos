"""
Len, Abs, sum, round

# Len
len() -> retorna o tamanho (qtd de itens) de um iterável

"""

print(len('Geek University'))

print(len([1, 2, 3, 4, 5]))

print(len((1, 2, 3, 4, 5)))

print(len({1, 2, 3, 4, 5, 5})) # conjunto não aceita repetição de elementos
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))

# Por debaixo dos panos, quanto usamos a função len(), o Python faz o seguinte:

# Dunder (double under) len
print('Geek University'.__len__())

# abs() -> retorna o valor absoluto de um número inteiro ou real. De forma báscica, seria o seu valor real sem o sinal
print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

# Sum

# sum() -> recebe como parametro um iterável, podendo reveber um valor inicial,  e retorna a soma total dos elementos
# incluindo o valor inicial
# não funciona com strings
# obs: o valor inicial default é zero

# Exemplos
print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))
print(sum([1, 2, 3, 4, 5], -5))

print(sum((1, 2, 3, 4, 5), -5))     # tupla
print(sum({1, 2, 3, 4, 5}, -5))     # set

print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values(), -5))   # set

# Round
# round() -> retorna um número arredondado para n digito de precisão após a casa decimal.
#Se a precisão não for informada, retorna o inteiro mais próximo da entrada

# Exemplos Round

print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.21212121, 2))
print(round(1.2199999, 2))
