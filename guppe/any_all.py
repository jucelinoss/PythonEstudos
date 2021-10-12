"""
Any e All

all() - retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio

# Exemplo all()

print(all([0,  1, 2, 3, 4 ])) # 0 é false -> false

print(all([ 1, 2, 3, 4 ])) # todos são verdadeiros

print(all([])) #True

print(all(( 1, 2, 3, 4 ))) # todos são verdadeiros

print(all({1, 2, 3, 4 })) # todos são verdadeiros

print(all('Geek')) # True

nomes = ['Carlos', 'Camila', 'Carla', 'CAssiano', 'Cristina']

print(all([nome[0] == 'C' for nome in nomes]))


nomes = ['Carlos', 'Camila', 'Carla', 'CAssiano', 'Cristina', 'Daniel']
print(all([nome[0] == 'C' for nome in nomes]))


print(all([letra for letra in 'eiod' if letra in 'aeiou']))

#
print([letra for letra in 'eio' if letra in 'aeiou'])
# list comprehension não deve ser usada para verificar se algum
# item não esta na lista

print(all([num for num in [ 4,2, 10, 6, 8,1] if num % 2 ==0]))
# retorna apenas os pares na list comprehension, que por sua vez retornam true (false somente se a lista tiver 0)

any() -> retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False
"""

print(any([0, 1, 2, 3, 4]))     # True
print(any([0, False, {}, (), []]))     # False

nomes = ['Carlos', 'Camila', 'Carla', 'CAssiano', 'Cristina', 'Daniel']

print(any([nome[0]== 'C' for nome in nomes]))

print(any(num for num in [4, 1, '0, 8, 8, 9'] if num % 2 == 0 ))
