"""
Listas

Listas em Python funcionam como vertores/matrizes em outras linguagens, com a diferenteça de serem DINÂMICOS
e também aceitarem QUALQUER tipo de dado.
são mutáveis

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;

Linguagem Python:
    - Dinâmico: não possui tamanho ou tipo de dado fixo;
    - o espaço disponível é a quantidade de memória
As listas em python são representadas por colchetes: []


# <class 'list'>
# print(type([]))

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')

# podemos facilmente se determinado valor está contido na lista
# num = 8

# if num in lista4:
#     print(f'{num} encontrado na lista4: {lista4}')
# else:
#     print(f'{num} não encontrado na lista4: {lista4}')
# Ordenar lista
# lista5.sort()
# print(lista5)
# print(lista5.count('e'))

# Adicionar elementos em listas


Para adicionar elemetnos em listas, utilizamos a função append
append adiciona um unico elemento por vez


print(lista1)
lista1.append(42)
print(lista1)
# adicionar uma lista dentro de outra
lista1.append([8, 3, 1])
# print(lista1)

#if [8, 3, 1] in lista1:
#    print('lista encontrada dentro de outra')
#else:
#    print('lista não encontrada dentro de outra')

#if [2, 27, 28] in lista1:
#    print('lista encontrada dentro de outra')
# else:
#     print('lista não encontrada dentro de outra')

# extend também permite adicionar um elemento à lista
# lista1.extend([123, 44, 67])
# ao adicionar uma lista dentro de outra, os elementos são adicionados separadamente
# print(lista1)


# append - coloca listas e elementos  como elementos únicos (sublista)
# extend - coloca listas como valor adicionais (mesmo nível); não aceita valores únicos
# lista1.extend(2) TypeError: 'int' object is not iterable
# lista1.extend([2])   # aceita listas, strings e outros objetos iteráveis
# lista1.extend('Geek')   # aceita listas, strings e outros objetos iteráveis
# print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
lista1.insert(2, 'Novo Valor')
print(lista1)

# Para juntar duas listas
lista6 = lista1 + lista2
print(lista6)

lista1.extend(lista2)
print(lista1)


lista1.reverse()    # reverte a ordem da lista
print(lista1)
# ou com slice
print(lista1[::-1])

# Copiar uma lista - lista.copy()
lista6 = lista2.copy()
print(lista6)

# Tamanho de uma lista len(lista)
print(len(lista2))

# Remover o último elemento da lista - lista.pop() e retorna o último elemento retornado
print(lista5)
lista5.pop()
print(lista5)

# Remover elemento pelo índice e desloca os elementos restantes para a esquerda
lista5.pop(2)
print(lista5)
# lista.pop(indice) retorna erro (Index Error) se não houver elementos na posição informada

# Remover todos os elementos da lista
lista5.clear()
print(lista5)

#
nova = [1, 2, 3]
type(nova)
nova *= 3
print(nova)

# Converter string para lista
curso = 'Programacao em Python Essencial'
print(curso)
curso = curso.split()   # por padrão, o split separa os elementos da lista pelo espaço entre elas
print(curso)

# Converter string para lista
curso = 'Programacao,em,Python,Essencial'
print(curso)
curso = curso.split(',')   # por padrão, o split separa os elementos da lista pelo espaço entre elas
print(curso)

# Converter lista para string
lista6 = ['Programacao', 'em', 'Python', 'Essencial']
print(lista6)

# concatena cada elemento da lista com espaço
# coloca espaço entre cada elemento e tranforma em uma string
curso = ' '.join(lista6)
print(curso)

# lista com tipos variados
# podemos colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados
lista6 = [1, 2.34, True, 'Geek', [1, 2, 3], 4534521]

# iterando sobre listas
# Exemplo 1 - utilizando for
soma = 0
for elemento in lista4:
    soma += elemento
print(soma)

# Exemplo 2 - utilizando while
soma = 0
carrinho = []
produto = ''
while produto != 'sair':
    print("Adicione um produo na lista ou digite 'sair' para sair:")
    produto = input()
    carrinho.append(produto)

for produto in carrinho:
    print(produto)



# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada

#           0        1           2       3
#          -4       -3          -2      -1
cores = ['Verde', 'amarelo', 'azul', 'branco']
print(cores[0])     # verde
print(cores[1])     # amarelo
print(cores[2])     # azul
print(cores[3])     # branco


# Fazer acesso aos elementos de forma indexada inversa
# para entender melhor o índice negativo, pensa na lista como um círuclo, onde
# o final de um elemento está ligado ao início da lista
print(cores[-1])    # branco
print(cores[-2])    # azul
print(cores[-3])    # amarelo
print(cores[-4])    # verde


cores = ['Verde', 'amarelo', 'azul', 'branco']
for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

cores = list(enumerate(cores))
print(cores)

# Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(42)

print (lista)

# Outros métodos não tão imporatnes mas tabém úteis
# Encontrar o índice de um elemento da lista
numeros = [5, 6, 7, 8, 9, 10, 5]
print(numeros.index(8))
# retorna erro se não encontrar na lista (ValueError)
print(numeros.index(5))     # retorna o primeiro item da lista se for procurado um elemento repetido

# Podemos fazer busca dentro de um range, ou seja, qual índice começar a buscar
print(numeros.index(5, 1, 2)) # index(valor_buscado, casa inicial, casa final)

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 6, 8))   # buscar o ´´indice de valor 8, dentro do intervalo de indices informado (inicio e fim)

# Revisão do slicing

# lista[inicio:fim:passo]
# range(inicio:fim:passo)


lista = [1, 2, 3, 4]
# Trabalhando com slice de listas com o parametro 'início'
print(lista[1:])    # iniciando no indice 1 e pegando todos os elementos restantes
print(lista[-1:])    # iniciando no indice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com o parãmetro 'fim'
print(lista[:2])   # começa em 0, pega até o índice 2 - 1
print(lista[:4])   # começa em 0, pega até o índice 4 - 1
print(lista[1:3])   # começa em 0, pega até o índice 4 - 1

print(lista[0:-1])   # começa em 0, pega até o índice 4 - 1

# Trabalhando com slice de lista com o parãmetro 'passo'
print(lista[1::2])  # Começa em 1, vai até o final, de 2 em 2

print(lista[0:0:2])     # Começa em 0, vai até o final, de 2 em 2
print(lista[1::-1])

nome = 'Programação em python essencial'
print(nome[::-1])


# Invertendo valores em uma lista
nomes = ['Geek', 'university']
# nomes[0], nomes[1] = nome[1], nome[0] # não reverte devidamente
print(nomes)
nomes.reverse()
print(nomes)

# Soma*, valor maximo*, valor minimo*, tamanho
# * Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista))    # soma
print(max(lista))    # maximo valor
print(min(lista))    # minimo valor
print(len(lista))    # tamanho da lista
"""
# transformar lista em tupla
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))
# listas são craidas a partir de colchetes, enquanto tuplas são craidas a partir de parêntesis

# Desempacotamento de listas
lista = [1, 2, 3]
num1, num2, num3 = lista     # a quantidade de variaveis deve ser igual a de itens da lista
print(num1)
print(num2)
print(num3)

# copiando uma lista para outra (Shallow copy e deep copy)

# Forma 1 - Deep copy
lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)
print(lista)
print(nova)

# ao utilizarmos lista.copy(), copiamos os dados da lista para uma nova lista, de forma independente
# as modificações de uma lista não alteram a outra (Deep copy em Python)

# Forma 1 - shallow copy
lista = [1, 2, 3]
print(lista)

nova = lista # cópia da referencia da memória

print(nova)
nova.append(4)
print(lista)

# ao atribuir uma lista em outra, a nova lista faz referencia ao endereço de memória da lista anterior.
# Dessa forma, qualquer alteração em uma lista será refletida na outra (Shallow Copy)



