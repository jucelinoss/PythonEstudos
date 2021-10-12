"""
Modos de abertura de arquivo
r-> leitura
w -> escrita -> sobrescreve dados se o arquivo existir

http://docs.python.org/3/library/functions.html#open

Character -> Meaning
'r' -> open for reading (default)
'w' -> open for writing, truncating the file first
'x' -> open for exclusive creation, failing if the file already exists
'a' -> open for writing, appending to the end of the file if it exists
'b' ->  binary mode
't' -> text mode (default)
'+' -> open for updating (reading and writing) - não é colocado sozinho

"""
try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteúdo \n')
except FileExistsError:
    print('o Arquivo university.txt já existe')

with open('frutas.txt', 'a', encoding='UTF8') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair')
        if fruta != 'sair':
            arquivo.write('Teste de conteúdo \n')
        else:
            break



