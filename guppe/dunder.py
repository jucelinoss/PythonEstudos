"""
Dunder Name e Dunder Main

dunder - Double under

Dunder Name -> __name__

Dunder Main -> __main__

Em python, são utilizados dunder para criar funções, atributos, propriedades etc utilizando Double Under para
não gerar conflito com os nomes desses elementos na programação

# Na linguagem C, temos um programa da seguinte forma:
int main(){
    return 0;
}


# Na linguagem Java, temos um programa da seguinte forma:
public static void main(String[] args){

}

# Em Python, se executarmos um móduloPython diretamente na linha de comando, internomente o
Python atribuirá à variável __name__ o valor __main__, indicando que este módulo é o de execução principal

from funcoes_com_parametro import soma_impares
print(soma_impares([1 ,2, 3, 4, 5, 6]))
"""
import primeiro
import segundo

