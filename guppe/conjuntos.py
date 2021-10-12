"""
Conjuntos

- conjuntos em linguagem de programação fazem referência à teoria dos conjuntos da matemática
- cojuntos em python são chamados de set
- Sets não possuem valores duplicados
- sets não possuem valores ordenados
- elementos não são acessados via índice (não são indexados)
- podem ser usados quando precisamos armazenar elementos mas não nos importamos com a ordenação, chaves, valores e intes duplicados
- são referenciados em python com chaves {}

Diferença entre conjuntos(sets) e mapas (dicinários) em python:
- um dicionário tem chave/valor
- um conjunto tem apenas valor;

# Definindo um conjunto

# Forma 1:
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # o conjunto possui duplicidades
print(s)
print(type(s))

# Conjuntos criados ou adicionados com repetição terão seus valores repetidos ignorados

# Forma 2 - mais comum
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Determinar se um elemento está contido no conjunto
elem = 3
if elem in s:
    print(f'o elemento {elem} faz parte do conjunto {s}')



# Importante lembrar que além denão termos valores duplicados, não temos ordem
dados = '99,2,34,23,12,1,44,5,2,34'

# listas aceitam valores duplicados - 10 elementos
lista = list(dados.replace(' ', ',').split(','))
print(f'Lista: {lista} com {len(lista)} elementos')

# tuplas aceitam valores duplicados - 10 elementos
tupla = tuple(dados.split(','))
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# dicionarios não  aceitam valores duplicados - 8 elementos
dicionario = {}.fromkeys(dados.split(','), 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')

# conjuntos não  aceitam valores duplicados - 8 elementos
conj = set(dados.split(','))
print(f'Conjunto: {conj} com {len(conj)} elementos')

# Assim como todo outro conjunto Python, podemos colocar tipos de dados misturados em sets

s = {1, 'b', True, '34.22, 44'}
print(s)
print(type(s))

# podemos iterar sets
for valor in s:
    print(valor)


# Usos interessantes com sets
# Em um formulario de cadastro de visitantes em uma feira ou museu,
# os visitantes informam manualmente a cidade de onde vieram
# Nós adicionamos cada cidade em uma lista Python,
# já que em uma lista podemoa dicionar novos elementos e ter repetição

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiabá', 'Campo Grande', 'São Paulo', 'Cuiabá']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas existem
# Basta converter para conjunto
print(len(set(cidades)))



# adicionar elementos em um conjunto (são mutáveis)
s = {1, 2, 3}
s.add(4) # não gera erro se o valor for repetido
print(s)


# Remover elementos de um conjunto
s = {1, 2, 3}
print(s)

# Forma 1
s.remove(3)     # o argumento passado é do valor a ser removido (conjuntos não são indexados)
print(s)
# retorna erro se o valor não for encontrado (KeyError)

# Forma 2

s.discard(2)    # o argumento passado é do valor a ser removido (conjuntos não são indexados);
# não retorna erro se o valor a ser removido não estiver na lista;
# não retorna o valor removido
print(s)

# Copiar um conjunto para outro
s = {1, 2, 3}
# Forma 1 - Deep copy
novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow copy
novo = s
novo.add(4)
print(novo)
print(s)


# Remover todos os elementos de um conjunto
s.clear()
print(s)


# Operações entre conjuntos
# Conjunto P: estudantes do curso de Python
# Conjunto J: estudantes do curso de Jython
estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo',  'Julia', 'Ana'}

# veja que alguns alunos de python tbm estudam java
# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Union
unicos = estudantes_python.union(estudantes_java)
print(unicos)

unicos = estudantes_java.union(estudantes_python)
print(unicos)

# Forma 2 - Utilizando pipe |

unicos2 = estudantes_java | estudantes_python
# pipe é menos intuitivo do que .union para uniao entre conjuntos
print(unicos2)

# Estudantes que estão em ambos os cursos
# Forma 1 - Insertection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - E comercial &

ambos2 = estudantes_python & estudantes_java
print(ambos2)

# gerar um conjunto de estudantes que não estão no outro curso

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo',  'Julia', 'Ana'}

so_python = estudantes_python.difference(estudantes_java)
print(f'somente python {so_python}')
so_java = estudantes_java.difference(estudantes_python)
print(f'somente java {so_java}')

"""
# Soma*, valor max*, valor min*, tamanho
# * se os valores forem todos inteiros ou reais
s = {1, 2, 3, 4, 5, 6}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))
