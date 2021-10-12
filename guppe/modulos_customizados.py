"""
Módulos customizados

Como módulos Python nada mais sao do que arquivos Python, então todos os arquivos que criamos neste curso são módulos
 python prontos para serem utilizados

"""

# import soma_impares ( temos acesso a todos os elementos do módulo)
# from funcoes_com_parametro import soma_impares

from funcoes_com_parametro import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))

from map import cidades, c_para_f

print(list(map(c_para_f)))
print(list(map(cidades)))
