"""
    Módulo Collections - ordered dict
ordered dict - dicionário que garante a ordem de inserção dos elementos
"""

from collections import OrderedDict

# Em um dicionário, a ordem de inserção dos elementos não é garantida
dicionario = {'a': 1, 'c': 3, 'b': 2, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave={chave} : valor={valor}')

# Ordered dict - as chaves ficam ordenadas no dicionário

dicionario = OrderedDict({'a': 1, 'c': 3, 'b': 2, 'd': 4, 'e': 5})
print(dicionario)

for chave, valor in dicionario.items():
    print(f'chave={chave} : valor={valor}')

# diferença entre dict e ordered dict
# Dicionários comuns -
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)

# True -> a ordem não importa

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})
print(odict1 == odict2)
print(odict1)
print(odict2)
# False - a ordem importa para o ordered dict

