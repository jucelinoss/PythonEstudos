"""
Sistema de arquivos - manipulação

"""

import os

# Verificar existencia de arquivo ou diretorio
# arquivo
print(os.path.exists('arquivo.txt'))
print(os.path.exists('frutas.txt'))
# diretório
print(os.path.exists('geek'))

# Criar arquivo
# Forma 1
open('arquivo-teste.txt', 'w').close()

# Forma 2
open('arquivo-teste.txt', 'a').close()

# Forma 3
with open('arquivo-teste.txt', 'a') as arquivo:
    arquivo.write('Escrita1')
    pass # não faz nada

# Forma recomendada (mknod não funciona no windows)
# os.mknod('arquivo-teste2.txt') # ou caminho absoluto
# os.mknod('arquivo-teste3.txt')

# o método mknod retorna FileExistsError caso exista

# Criação de diretórios (retorna erro se já existir a pasta ou se não tiver permissão de criação)
os.mkdir('template') # cria um único arquivo por vez

# Criação de multiplos diretórios (arvore) - nao funciona no windows
# os.mkdirs('templates/geek/university', exist_ok=True)



