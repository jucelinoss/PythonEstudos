"""
    Escrita de arquivos

# open() por padrão abre o arquivo no modo de leitura
#OBS.: ao abrir um arquivo para leitura, não podemos realizar escrita. Da mesma forma, se abrirmos um arquivo
para escrita, não podemos lê-lo
Ao abrir um arquivo para escrita, o arquivo é criado no sistema de arquivos, caso não exista. Se existir, o conteúdo é
sobrescrito


# Exemplo de escrita pythônica - (w) -> sobrescreve os dados no novo arquivo
with open('novo.txt', 'w', encoding='UTF-8') as arquivo:
    arquivo.write('Teste de escrita de arquivos em python\n')
    arquivo.write('Podemos colocar quantas linhas quisermos\n')
    arquivo.write('Esta é a última linha\n')

# exemplo de gravação não pythônico - tradicional
arquivo = open('mais.txt','w')

arquivo.write('TEXTO QUALQUER\n')
arquivo.write('MAIS UM TEXTO QUALQUER\n')
arquivo.close()



with open('geek.txt', 'w') as arquivo:
    arquivo.write('Geek ' * 1000)
"""


with open('frutas.txt','w', encoding='UTF-8') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair:')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break


