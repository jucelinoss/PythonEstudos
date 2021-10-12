"""
Seek e cursor

seek() - usada para movimentar o cursor pelo arquivo.
Recebe um parâmetro indicando a posição onde o cursor seja posicionado  (posição atual + acumulado de linhas anteriores)
arquivo = open('texto.txt')

print(arquivo.read())

# Movimentar o cursor pelo arquivo através da função seek

arquivo.seek(22)

print(arquivo.read())

# readline() - lê o arquivo linha a linha -> retorna string

print(arquivo.readline())
print(arquivo.readline())

Obs: quando abimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco do computador e o
programa. Essa conexão é chamada de stream. Ao finalizar o trabalho, deve-se fechar a conexão, através da função close()

# readlines() -> adiciona cada linha em uma lista de string
print(arquivo.readlines())

# mostrar a qtd de linhas
print(len(arquivo.readlines()))


Passos para se trabalhar com um arquivo
1 - Abrir o arquivo
arquivo = open('texto.txt')

2 - trabalhar com o arquivo
print(arquivo.read())

3 - Fechar o arquivo
arquivo.close()

# 1 - abrir arquivo
arquivo = open('texto.txt')

# 2 - trabalhar com o arquivo
print(arquivo.read())

# 3 - Fechar o arquivo
arquivo.close()

# tentativa de leitura após fechamento (ValueError: I/O operation on closed file.)
# print(arquivo.read())


# Verificar se um arquivo está fechado antes de fechar
if not arquivo.closed:
    arquivo.close()
    print('o arquivo estava aberto')
else:
    print('o arquivo estava fechado')

"""

arquivo = open('texto.txt')
print(arquivo.read(15)) # le os X primeiros caracteres





