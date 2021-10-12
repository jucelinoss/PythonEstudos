"""
Mapas - conhecidos em python como dicionários

Dicionários em python são representados por chaves {}

receita = {'jan': 100, 'fev': 250, 'mar': 400 }

# Iterar sobre dicionários
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])


for chave in receita:
    print(f' Em {chave} recebi ${receita[chave]}')

# Acessar chaves
print(receita.keys())

# Modo pythônico
for chave in receita.keys():
    print(receita[chave])


receita = {'jan': 100, 'fev': 250, 'mar': 400 }


# acessar valores do dicionário

print(receita.values())

for valor in receita.values():
    print(valor)

"""
receita = {'jan': 100, 'fev': 250, 'mar': 400 }

# Desempacotamento de dicionários
for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')


# Soma*, valor max*, valor min*, tamanho
# * se os valores forem numéricos (inteiros ou reais)

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))




