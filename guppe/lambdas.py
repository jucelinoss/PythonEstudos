"""
Utilizando Lambdas
 - são funções sem nome (anônimas)





# função em python
def funcao(x):
    return 3 * x + 1


print(funcao(3))
print(funcao(7))

# Expressão lambda
calc = lambda x: 3 * x + 1 # não é forma ideal de uso de lambdas

print(calc(3))
print(calc(7))

# Podemos ter expressões lambda com múltiplas entradas
nome_completo = lambda  nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

# str.strip() -> equivalente ao comando trim

print(nome_completo('angelina', 'JOLIE'))
print(nome_completo(' FELICITY   ', '  jones  '))
"""


# Em funções Python, podemos ter nenhuma ou várias entradas. Em lambdas também

# formato antigo
# n = lambda x1, x2, .... nx: <expressão>
# amar = lambda: 'Como não amar Python?'
# uma = lambda x: 3 * x + 1
# duas = lambda x, y: (x * y) ** 0.5
# tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

# formato novo
# def n(params): return <expressão>
def amar(): return 'Como não amar Python?'


def uma(x): return 3 * x + 1


def duas(x, y): return (x * y) ** 0.5


def tres(x, y, z): return 3 / (1 / x + 1 / y + 1 / z)


print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))
# Se passarmos mais argumentos do que parametros esperados teremos TypeError

# Outro Exemplo

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert',
           'Orson Scott Card', 'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']
# extrair ultimo sobrenome em ordem alfabética
sobrenome_autores = [autor.split(' ')[-1] for autor in autores]
sobrenome_autores.sort()
print(sobrenome_autores)

# ou ordenar nomes a partir de sobrenomes
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)


# Função quadrática
# f(x) = a * x ** 2 + b * x + c

# Definindo a função
def geracao_fn_quadratica(a, b, c):
    """
    Retorna a função f(x) = a * x ** 2 + b * x + c
    """
    return lambda x: a * x ** 2 + b * x + c

teste = geracao_fn_quadratica(2, 3, -5)
print(teste(0))
print(teste(1))
print(teste(2))

#ou
print(geracao_fn_quadratica(2, 3, -5)(0)) # o elemento do 2o parenteses é o valor de x
print(geracao_fn_quadratica(2, 3, -5)(1))
print(geracao_fn_quadratica(2, 3, -5)(2))

# Aplicações lambdas
# usadas em filtragem e ordenação de dados
