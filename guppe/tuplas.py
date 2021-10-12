"""
Tuplas (tuple)

Tuplas são parecidas com listas
Existem duas diferenças básicas:

1 - As tuplas são representadas por parênteses
    print(type( (1) ))
    <class 'tuple'>
2 - São imutáveis. Ao se criar ou alterar uma tupla, é gerada uma nova:


lista = [9, 4, 1, 6, 3]
lista.sort()

# CUIDADO1: as tuplas são representadas por parêntesis
tupla = (1, 2, 3, 4, 5, 6)
print(tupla)
print(type(tupla))

tupla1 = 1, 2, 3, 4, 5, 6   # sem parentesis tbm são consideradas tuplas
print(tupla)
print(type(tupla))

# CUIDADO 2: Tuplas com um elemento
tupla3 = (4)    # tupla com um único elemento não é uma tupla
print(type(tupla3))

# CUIDADO 2: Tuplas com um elemento
tupla4 = (4, )    # isso é uma tupla
print(type(tupla4))
# tuplas são definidas pela virgula e não pelo uso de parênteses

tupla5 = 4,     # isso é uma tupla
print(type(tupla5))
# tuplas são definidas pela virgula e não pelo uso de parênteses

# (4)   -> não é tupla
# (4,)  -> é tupla
# 4,    -> é tupla

# Podemos gerar uma tupla dinamicamente com range(inicio, fim, passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla
tupla = ('Geek University', 'Programação em Python: Essencial')
escola, curso = tupla
print(escola)
print(curso)

# Obs.: gera erro (valueError) se colocarmos um número diferente de elementos para desempacotar

# Métodos para adição, remoção de elementos em tuplas não existem, dado o fato de serem imutáveis
# Soma*, valor máximo*, valor mínimo* e tamanho
tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla))   # 21
print(max(tupla))   # 6
print(min(tupla))   # 1
print(len(tupla))   # 6

# Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2) # tuplas são imutáveis
print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2 # tuplas são imutáveis, mas podemos sobrescrever seus valores
print(tupla1)


# Verificar se determinado elemento está contido na tupla
tupla = (1, 2, 3)
print(3 in tupla)

# iterar sobre uma tuppla

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)


# Contar elementos dentro de uma tupla
tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('a'))

escola = tuple('Geek university')
print(escola)
print(escola.count('e'))

"""

# Dicas na utilização de tuplas
# Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção
# Exemplo 1
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril',  'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# não faz sentido permitir a adição de novos valores para este domínio

# O Acesso de elementos de uma tupla também é semelhante ao de uma lista
# print(meses[5])

# Iterar com while
i = 0
while i < len(meses):
    print(meses[i])
    i += 1


# Verificar em qual posição um elemento está na tupla
print(meses.index('Janeiro')) # A função index funciona da mesma forma para listas e tuplas
# retorna erro se não estiver na lista

# Slicing
# tupla (inicio:fim:passo)
print(meses[0:]) # todos os meses
print(meses[5:9]) # jun a set

# Por quê utilizar - Tuplas
# 1 - tuplas são mais rápidas do que listas
# 2 - tuplas deixam seu código mais seguro. Trabalhar com elementos imutáveis traz segurança para o código

# Copiando uma tupla para outra
tupla = (1, 2, 3)
print(tupla)
nova = tupla     # mesmo ID (ambas referenciam mesmo espaço na memória); na tupla não temos o problema de shallow copy

print(id(nova))
print(id(tupla))
print(nova)
print(tupla)

outra = (4, 5, 6)
nova += outra

print(id(nova))
print(id(tupla))
print(nova)
print(tupla)

lista = [1, ]   # lista
print(type(lista))
tupla = 1,      # tupla
print(type(tupla))























