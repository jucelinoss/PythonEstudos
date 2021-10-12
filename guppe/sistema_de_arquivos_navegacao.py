"""
Sistema de arquivos e navegação

Para manipular arquivos do SO, importamos o módulo os

os -> operating system

cwd

import os


# getcwd() - retorna o cwd (current work directory)
# Retorna o path absoluto
print(os.getcwd())

# Para mudar o diretório, podemos usar chdir()
os.chdir('..')
print(os.getcwd())

# Podemos checar se uym direório é absoluto ou relativo
print('ABS path Unix: '+os.path.isabs('/home/geek').__str__())

# Obs para windows: deve-se tomar cuidado ao verificar diretórios

print('ABS path  win:' + os.path.isabs('C:\\Users\\Public\\Music').__str__())

# Podemos identificar o SO
print(os.name) # posix (Linux/ Mac), nt (windows)
#detalhes adicionais


#print(os.uname())

1
Unfortunately, the uname function only works on some Unix systems. If you are on Windows, you can use the uname function in the platform module, which returns a similar result.
>>> import platform
>>> print(platform.uname())
uname_result(system='Windows', node='DESKTOP-OVU16P3', release='10', version='10.0.19042',

import platform
print(platform.uname())

# criar diretório
#
"""
import os


# recebe 2 params (diretorio desejado , diretório que será adicionado ao desejado)
res = os.path.join(os.getcwd(), 'geek', 'university')
# os.mkdir('geek') -> não cria diretório existente; lança msg de erro
os.chdir(res)
print(os.getcwd())

# Listar arquivos e diretórios (retorna em lista)
print(os.listdir())
# qtd de itens dentro da pasta
print(len(os.listdir()))

scanner = os.scandir(os.getcwd())
arquivos = list(scanner)

print('Lista de objetos dentro do diretório' + arquivos.__str__())
print('Inode' + str(arquivos[0].inode())) # ID do nó na arvore de diretórios
print('É arquivo: ' + str(arquivos[0].is_file()))
print('É diretorio: ' + str(arquivos[0].is_dir()))
print('É atalho: ' + str(arquivos[0].is_symlink())) # link simbolico (atalho)
print('Nome: ' + arquivos[0].name)
print('Caminho:' + arquivos[0].path)
print('Metadados: ')
print(arquivos[0].stat())

# OBS.: quando usamos a funcao scandir(), precisamos fechá-la

scanner.close()