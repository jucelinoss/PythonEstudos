"""

Filter

Filter() -> permite filtrar dados de uma determinada coleção


import statistics
valores = 1, 2, 3, 4, 5, 6
media = sum(valores)/len(valores)

print(f'Média:{media}')

# dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(f'Média:{media}')

# Obs. Assim como a função map(), a função filter() recebe dois parametros (uma função e um iterável)
res = filter(lambda x: x > media, dados)
print(list(res))
print(type(res))

# assim como na função map(), após o uso dos dados de filter(), estes são excluídos da memória
"""

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colômbia', '', 'Equador', '', '', 'Venezuela']
res = filter(None, paises) # remove elementos vazios da lista
print(list(res))
# ou
res = filter(lambda pais: len(pais) > 0, paises) # remove elementos vazios da lista
print(list(res))
# ou
res = filter(lambda pais: pais != '', paises) # remove elementos vazios da lista
print(list(res))

print('' == None) # '' não é None

# A diferença entre map() e filter() é
# map() -> recebe dois parametos, função e iterável; retorna um objeto mapeando a função para cada elemento do iterável
# filter () -> recebe dois parametos, função e iterável; retorna um objeto filtranso apenas os elementos que atendem o predicado

# Exemplo mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "Carla", "tweets": ["Eu amo meu gato"]},
    {"username": "Jeff", "tweets": []},
    {"username": "Bob123", "tweets": []},
    {"username": "Doggo", "tweets": ["Eu gosto de cachorros", "vou sair hoje"]},
    {"username": "Gal", "tweets": []}
]
print(usuarios)
# Filtrar os usuários que estão inativos no Twitter

# Forma 1
inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
print(inativos)

# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos)

# bool([]) -> False
# bool(['a']) -> True

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Criar lista contendo 'Sua instrutora é' + nome,  desde que cada nome tenha menos de 5 caracteres
lista = list(map(lambda nome: f'Sua instutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)

