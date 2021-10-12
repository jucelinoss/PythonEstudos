"""
Generator expression
- nome dado as tuple comprehensions


nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any(nome[0]=='C' for nome in nomes])


nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes])) # any(expressao_generator)

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator - consome menos recursos de memória
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)


from  sys import getsizeof

# getsizeof -> retorna a quantidade de bytes do elemento informado no parâmetro
print(getsizeof('Geek'))
print(getsizeof('University'))
print(getsizeof(9))
print(getsizeof(92345668823))
print(getsizeof(True))
"""
from sys import getsizeof

# Geração de lista de numeros com list comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])
print(f'Espaco de uma list Comprehension ate 1000: {list_comp} bytes')
set_comp = getsizeof({x * 10 for x in range(1000)})
print(f'Espaco de uma set Comprehension ate 1000: {set_comp} bytes')
dict_comp = getsizeof({x: x * 10 for x in range(1000)})
print(f'Espaco de uma dict Comprehension ate 1000: {dict_comp} bytes')

# geração de lista de numeros com generator
gen = getsizeof(x * 10 for x in range(1000))
print(f'Espaco de um generator ate 1000: {gen} bytes')

# Iteração no Generator Expression
gen = (x * 10 for x in range(1000))
for num in gen:
    print(num)


