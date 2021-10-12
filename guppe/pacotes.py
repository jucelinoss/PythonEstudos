"""
Módulo -> arquivo python que pode ter diversas funções para utilizarmos
Pacote -> diretório com coleção de módulos
Nas versões 2.x do Pytho, um pacote python deveria conter dentro dele um arquivo chamado __init__.py
Nas versões 3.x do Python,não é mais obrigtório o uso deste arquivo, mas ainda é usado para manter
compatibilidade



"""

from geek import geek1, geek2
print(geek1.pi)

print(geek1.funcao1(4, 6))

print(geek2.curso)


from geek.university import geek3, geek4

print(geek3.funcao3())
print(geek4.funcao4())