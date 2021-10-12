"""
Dicionários
- são conhecidos por mapas em algumas linguagens de programação
- são coleções do tipo chave/valor
- são representados por chaves {}
- chave e valor podem ser de qualquer tipo
- pode-se misturar tipos de dados

print(type({}))
# <class 'dict'>

# Criação de dicionários
# Forma1 (mais comum)

paises = {
            'br': 'Brasil',
            'eua': 'Estados Unidos',
            'py': 'Paraguai'
          }
# : separam a chave do valor {chave1:valor1, chave2:valor2}
print(paises)
print(type(paises))

# Forma 2 ( Menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

# Acessar elementos
# Forma 1 - Acessar via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])
print(paises['ru'])     # chave não cadastrada gera KeyError

paises = {
            'br': 'Brasil',
            'eua': 'Estados Unidos',
            'py': 'Paraguai'
          }
# Forma 2 - acessando via get - Recomendada
# print(paises.get('br'))
# print(paises.get('ru'))     # retorna o valor None se não for encontrada a chave (nçao provoca keyError)

chavePais = 'ru'
pais = paises.get(chavePais)
if pais :
    print(f'{pais} encontrado')
else:
    print(f'Chave {chavePais} não encontrada')

# captura com valor padrão caso a chave não seja encontrada
chavePais = 'ru'
pais = paises.get(chavePais, 'Não encontrado')
print(f'Encontrei o país {pais}')

# Busca por chaves - podemos verificar se determinada chave se encotnra em um dicionário
# chave in dicionario
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# podemos usar qualquer tipo de dado, inclusive coleções (tupla, dicionario, lista) como chaves de dicionários


# Tuplas são um exemplo interessante de uso como chave de dicionários, pois são imutáveis
localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}
# as localidades são meros exemplos e podem não refletir a realidade;
# já que não mudam, as chaves podem ser armazenadas como tuplas
print(localidades)
print(type(localidades))


# Adicionar elementos a um dicionário
receita = {
        'jan': 100,
        'fev': 120,
        'mar': 300
}

print(receita)
print(type(receita))

# Forma 1 - mais comum
receita['abr'] = 350
print(receita)

# Forma 2 - menos comum
novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)

# atualizando dados em um dicionário
# o método update permite inserir ou atualizar dados no dicionário
receita.update({'jun': 450})
receita.update({'jun': 600})
print(receita)

# Em dicionários, não podemos ter chaves repetidas


# Remover dados de um dicionário

receita = {
        'jan': 100,
        'fev': 120,
        'mar': 300
}
# Forma 1 (mais comum)

receita.pop('mar')  # remove a chave; retorna key error se nao encontrar
print(receita)

# ao removermos um objeto, o comando pop retorna o valor do elemento removido da coleção

# Forma 2
del receita['fev']
print(receita)
del receita['jan'] # o comando del não retorna o valor removido
print(receita)

"""

# caso de uso - dicionários
# Carrinho de compras e-commerce
"""
Carrinho de compras:
    produto 1:
        - nome;
        - qtd;
        - preço
    produto 2:
        - nome;
        - qtd;
        - preço

# Forma 1 - lista
# Podemos armazenar no fomato de lista
carrinho1 = []
produto1 = ['PS4', 1, 2300.0]
produto2 = ['God of war 4', 1, 150.0]

carrinho1.append(produto1)
carrinho1.append(produto2)

# teríamos que saber qual o indice de cada informação no produto

# Forma 2 - tupla
# Podemos armazenar no fomato de lista
carrinho2 = ()
produto1 = ('PS4', 1, 2300.0)
produto2 = ('God of war 4', 1, 150.0)

carrinho2 = (produto1, produto2)
# teríamos que saber qual o indice de cada informação no produto

# Forma 3 - dicionário
carrinho3 = []
produto1 = {'nome': 'PS4', 'qtd': 1, 'preço': 2300}
produto1 = {'nome': 'God of war 4', 'qtd': 1, 'preço': 150}

carrinho3.append(produto1)
carrinho3.append(produto2)

print(carrinho1)
print(carrinho2)
print(carrinho3)

# facilmente adicionamos ou removemos produtos no carrinho e em acada produto podemos ter a certeza de cada informação

# Métodos de manipulação de dicionários
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Limpar o dicionário
d.clear()
print(d)

# Copiar um dicionário para outro
# Forma 1
d = dict(a=1, b=2, c=3)
novo = d.copy() # Deep copy (copia dado do objeto)

print(novo)
novo['d'] = 4

print(d)
print(novo)

# Forma 2 - Shallow Copy
d = dict(a=1, b=2, c=3)
novo = d  # Shallow copy (copia dado do objeto)

print(novo)
novo['d'] = 4

print(d)
print(novo)

"""
# Forma não usual de criação de dicionários

outro = {}.fromkeys('a','b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método from keys recebe dois parâmetros: um iterável e um valor
# Gera uma chave para cada valor do iterável e atribui um valor a cada uma.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1,11), 'novo')
print(veja)
