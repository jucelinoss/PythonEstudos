"""
Tipo Float
Tipo real, decimal
Casas decimais

Obs.: o separador de casas decimais na programação é o mponto e não a vírgula

#Errado
valor = 1,44

print(valor)
#Certo
valor = 1.44
print(valor)
"""

#Errado
valor = 1,44
print(valor)
print(type(valor))

#Certo
valor = 1.44
print(valor)
print(type(valor))

# dupla Atribuição
print("Dupla atribuição")
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos coneverter um float para um int
"""
OBS.: Ao converter valores float para inteiros, nós perdemos precisão
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
compl = 5j
type(compl)

print(compl ** 2)

