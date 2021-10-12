"""
Um dado é considerado do tipo string sempre que estiver entre aspas simples, duplas ou triplas
Exemplos: '234', 'a','True', '42.2', "234", "a","True", "42.2",
Não existe caractere no python

"""
# string com aspas triplas """A""", """21"""

nome = "teste"
print(type(nome))
nome = 'teste'
print(type(nome))
nome = """teste"""
print(type(nome))

nome = "What's \nnew"
print(nome)
print(type(nome))

nome = "Angelina \" Jolie"
print(nome)
print(type(nome))

nome = 'Geek University'
print(nome.upper())
print(nome.lower())

print(f' {nome} em maiusc: {nome.upper()}')
print(f' {nome} em minusc: {nome.lower()}')

print(f' {nome} com split: {nome.split()}')

# [ 0,   1,   2,   3,  4,   5,  6,  7,  8,  9,  10, 11, 12, 13, 14]
# ['G', 'e', 'e', 'k',' ', 'U','n','i','v','e','r','s','i','t','y']
nome = 'Geek University'
print(nome[0:3]) # variavel[caractere_inicial, 1o caractere não incluído] - slice de string (string slicing)

print(nome[5:15])

# 1o item do split
print(nome.split()[0])

"""
[::-1] -> comece do primeiro elemento, vá até o último elemento e inverta
"""
# Inversão de Pythônica
print(nome[::-1])

print(nome.replace('e', 'P'))

# palindromo
texto = "socorram me subino onibus em marrocos"
print(texto[::-1])
