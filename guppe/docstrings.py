"""

Documentando funções com docstrings
- devemos documentar somente os itens essenciais

Obs.: podemos ter acesso a documentacao de uma função em pyhon utulizando a propriedade especial __doc__
Podemos ainda fazer acesso à documentação com a função help()
"""

print(help(print))

def diz_oi():
    """Uma função simples que retorna a string 'Oi!'"""
    return 'Oi'

# no python console, importar arquivo e acessar documentação da função
# from docstrings import diz_oi
# help(diz_oi())


def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de um número ou este elevado à potencia informada

    :param numero: valor da base a potência calculada
    :param potencia: valor do expoente calculado
    :return: retorna o exponencial de 'numero' por potencia
    """
    return numero ** potencia
