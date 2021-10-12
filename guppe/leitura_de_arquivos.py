"""
Leitura de Arquivos

Para ler o conteúdo de um arquivo em Python, utilizamos a função built-in (integrada) open()

open() -> Na forma mais simples de uso, passamos apenas um parâmetro de entrada (nome do arquivo a ser lido). A função
retorna um _io.TextIOWrapper, com o qual trabalhamos para manipular o conteúdo dos arquivos

http://docs.python.org/3/library/functions.html#open

#Obs.: por padrão, a função open() abre o arquivo para leitura. Caso não exista, é lançado o erro FileNotFoundError

variavel
 arquivo <_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>
 tipo: <class '_io.TextIOWrapper'>

"""

# Exemplo

arquivo = open('texto.txt')
print(arquivo)
print(type(arquivo))

# Para ler o conteúdo do arquivo, após sua abertura, usamos a fgunção read()

print(arquivo.read()) # a função read retorna uma string
# Obs.: o Python utiliza o recurso de cursor para trabalhar com arquivos. O Cursor se move conforme é realizada a
# leitura.
# Funciona como o cursor da digitação.

# A função read() lê todo conteúdo do arquivo
# Na segunda chamada, não há conteúdo para ler, pois o cursor chegou ao final do conteúdo do arquivo.
print(arquivo.read())
print(arquivo.read())
