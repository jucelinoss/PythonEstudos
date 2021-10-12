"""
String IO
Para ler ou escrever dados em arquivos do sistema operacional, o software precisa ter permissão
    - Permissão de leitura -> para ler dados do arquivo
    - Permissão de escrita -> para escrever dados no arquivo

StringIO -> Utilizado para ler e criar arquivos em memória
"""

# para usar String IO, fazemos a importação
from io import StringIO

mensagem = 'Esta é uma string normal'

# Podemos criar um arquivo em memoria ja com uma string ou vazio, para  inserir conteúdo depois
arquivo = StringIO(mensagem) # equivalente a arquivo = open('arquivo.txt', 'w')


# Utilização de String
print(arquivo.read()) # leitura de arquivo em buffer de memória
arquivo.write('Nova linha\n')
print(arquivo.read()) # leitura de arquivo em buffer de memória

# Podemos movimentar o cursor em arqivos que estão em buffer de memória
arquivo.seek(0)
print(arquivo.read()) # leitura de arquivo em buffer de memória

