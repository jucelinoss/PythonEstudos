"""
Zip

zip() -> cria um iterável (zip object) que agrega o elemento de cada um dos iteráveis passados como entrada em pares
"""

# Exemplos
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))

# Sempre podemos gerar uma Lista, Tupla ou Dicionário
# Após o uso, o objeto é descartado da memória
# print(list(zip1)) # lista com tuplas de cada correspondencia
# print(tuple(zip1))  # tupla com tuplas de cada correspondencia
#print(set(zip1))    # conjunto com tuplas de cada correspondencia
print(dict(zip1))   # dicionário com chave e valor (nao gera tupla interna)

# utiliza como parametro o menor tamanho em iterável. Ao trabalhar com iteráveis de tamanhos diferentes, irá parar
# quando os elementos do menor iterável acabar
lista3 = [7, 8,9, 10, 11]
zip1 = zip(lista1, lista2, lista3)
print(list(zip1))   # 1o objeto de cada lista + 2o objeto de cada lista + 3o objeto de cada lista

# Podeomos utilizar diferentes iteráveis com zip
tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Lista de tuplas
dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))    # desempacotamento

# Exemplos mais complexos
prova1 = [80, 91, 78]
prova2= [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']
final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

# ou
final2 = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final2))

media = {dado[0]: (dado[1] + dado[2])/2 for dado in zip(alunos, prova1, prova2)}
print(media)