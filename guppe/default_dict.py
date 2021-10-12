"""
Módulo collections - default dict
https://docs.python.org/3/library/collections.html#collections.defaultdict

# Recap dicionários

dicionario = {'curso': 'Programação em python Essencial'}

print(dicionario)
print(dicionario['curso'])
print(dicionario.get('outr')) # None

Default dict -> ao criar um dicionário default, informamos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver um valor definido.
Caso tentemos acessar uma chave que não existe, essa chave será criada e o valor default será atribuído.

Lambda - funções sem nome que podem receber ou não parametros de entrada e retornar valores
"""

# Default dict não retorna keyError em caso de chave inexistente

from collections import defaultdict

dicionario = defaultdict(lambda: 0)


dicionario['curso'] = 'Programacao em python essencial'
print(dicionario)

print(dicionario['outro'])
# não gera erro na busca por chave inexistente; adiciona a chave com valor defaul informado na definicao do dict

print(dicionario)

