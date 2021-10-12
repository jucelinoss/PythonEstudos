"""
Levantando os próprios erros com Raise

raise - lança exceções
- raise não é uma função, mas uma palavra reservada, assim como def em python
Para simplificar, pense no raise como um comando útil para customizae exceções e mensagens de erro.

Forma eral de utilização:
    raise TipoDoErro('Mensagem de Erro')

raise ValueError('Valor Incorreto')
OBS.: O raise, assim como o return, finalza a função. Nada após o raise é executado
"""

def colore(texto, cor):
    cores = 'verde', 'amarelo', 'azul', 'branco'

    if type(texto) is not str:
        raise TypeError('O texto precisa ser do tipo string')
    if type(cor) is not str:
        raise TypeError('A cor precisa ser do tipo string')
    if cor not in cores:
        raise ValueError(f'A cor recisa ser entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Geek', 'azul')

