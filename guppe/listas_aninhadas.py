"""
Listas aninhadas (Nested lists)

Algumas linguagens de programação como C e Java possuem estruturas de dados chamadas de arrays
- unidimensionais (arrays/vetores)
- multidimensionais (matrizes)
- arrays e matrizes possuem tamanho e tipo de dado limitado

Não existe vetor em python, mas listas (sem restrição de tamanho ou tipo de dado)
numeros = [1, 'bn', 3.234, True, 5]



# Exemplos
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # equivalente a uma matriz 3 x 3
print(listas)
print(type(listas))

# Acesso aos dados
print(listas[0][1]) # 2 - linha 0 e coluna 1
print(listas[2][1]) # 8 - linha 2 e coluna 1

# Iterando com loops em uma lista aninhada

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # equivalente a uma matriz 3 x 3

for lista in listas:
    for numero in lista:
        print(numero)

# list Comprehension
print('Lista aninhada com List Comprehension')
[[print(valor) for valor in lista] for lista in listas]
"""
# Outros exemplos

# Gerando um tabuleiro / matrix 3x3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['x' if numero % 2 == 0 else '0' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais
print([['*' for i in range(1, 4)] for j in range(1, 4)])
