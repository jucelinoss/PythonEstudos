"""
Método Collections - Named Tuple
https://docs.python.org/3/library/collections.html
tupla = (1, 2, 3)
print(tupla[1])

# tupla = (num1=1, num2=2, num33)
Named Tuple -> são tuplas diferencias, nas quais especificamos nome e parâmetros

"""
from collections import namedtuple

# definir nome e parâmetros

# Forma 1 - declaração de named tuple
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - declaração de named tuple
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - declaração de named tuple
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# utilização de namedtuple


ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')
print(type(ray))
# tipo de dado personalizado - análogo a um struct
print(ray)

# Acessando dados
# Forma 1
print(ray[0])
print(ray[1])
print(ray[2])

# Forma 2 - semelhante a structs
print(ray.idade)
print(ray.raca)
print(ray.nome)

print(ray.index('Chow-Chow'))
print(ray.count('Chow-Chow'))
