""""
Ranges
Precisamos conhecer o loop for para usar os ranges
Precisamos conhecer o range para trabalhar melhor com loops for


Ranges são utilizados para gerar sequências numéricas, não de forma aleatória, mas sim de maneira especificada

Formas gerais:

# Forma 1
range(valor_de_parada)
obs.: valor_de_parada não inclusivo (início padrão 0, passo de 1 em 1)

# Exemplo Forma 1
for num in range(10):
    print(num)

# Forma 2
range(valor_de_inicio, valor_de_parada)
obs.: valor_de_parada não inclusivo (início especificado pelo usuário, passo de 1 em 1)

# Exemplo Forma 2
for num in range(1, 11):
    print(num)

# Forma 3

range(valor_de_inicio, valor_de_parada, passo)
obs.: valor_de_parada não inclusivo (início especificado pelo usuário, passo especificado pelo usuário)

# Exemplo foma 3
for num in range(0, 55, 5):
    print(num)

# Forma 4 (inversa)
range(valor_inicio, valor_de_parada, passo)
obs.: valor_parada não inclusivo (início especificado pelo usuário, fim especificado pelo usuario. passo especificado pelo usuário)

# Exemplo forma 4
# iteração de 10 a 0 (-1 não é inclusivo)
for num in range(10, -1, -1):
    print(num)

"""
lista = range(10)     # salva o obj range

lista = list(range(10))    # cria uma lista com 10 itens
