"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python
The Zen of Python

import this
A ideia do PEP8 é que possamos escrever códigos Python de forma Pythônica

[1] - Utilize Came Case para nomes de classes:
        inicial maiuscula de cada palavra
[2] - Utilize nomes em minúsculo separados por underline para funções ou variáveis

[3] - Utilize 4 espaços para identação! (não é recomendado utilizar tab)
    tab pode ser configs diferentes e cada computador (é possível configurar para 5, 7 ou 12 espaços, por exemplo)
Python é totalmente dependente de indentação

[4] - Linhas em branco
    - Separar funções e definições de classe com duas linhas em branco;
    - Métodos dentro de uma classe devem ser separados com uma única linha em branco

[5] - Imports
    - devem ser sempre realizados em linhas separadas
    Exemplo
    # Errado
        import sys, os
    #Certo
        import sys
        import os

    # Não há problemas em utilizar importação de objetos:
    from types import StringType, ListType

    #Caso haja muitos imports de um mesmo pacote, recomenda-se fazer:
    from types import (
        StringType,
        ListType,
        SetType,
        OutroType
    )
    # Imports devem ser usados no topo do arquivo, depois de qualquer comentário ou docstrings e antes de constantes ou variáveis globais
     - comentários
     - imports
     - variáveis

[6] - Espaços em expressões e instruções
   #Não faça
        funcao( algo[ 1 ], { outro: 2} )
        algo (1)
        dic ['chave'] = list [indice]
        x               = 1
        y               = 3
        variavel_longa  = 5

    #Faça
        funcao(algo[1], {outro:2})
        algo(1)
        dic['chave'] = list[indice]
        x = 1
        y = 3
        variavel_longa = 5

[7] - Termine sempre uma instrução com uma nova linha (em branco)
    Exemplo linha 72

[8] - Comentários
    Comentários simples (uma linha): #
    Comentários de linhas compostas: 3 aspas duplas (recomendado) ou simples
"""

import this
