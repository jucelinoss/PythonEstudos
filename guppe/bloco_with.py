"""
 O Bloco with 
 
 Passos para se trabalhar com arquivos
 # 1 - Abrir o arquivo
 # 2 - Manipular o arquivo
 # 3 - Fechar po arquivo
 
 O bloco with é utilizado para criar um contexto de trabalho, no qual os recursos são fechados após o bloco
  
 """
# Bloco with (forma pythônica de se manipular arquivos
with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print("Arquivo aberto dentro do bloco with? " + arquivo.closed.__str__() )

print("Arquivo aberto fora do bloco with? " + arquivo.closed.__str__())
