"""
Módulo collections - Counter(contador)
https://docs.python.org/3/library/collections.html#collections.Counter
Conhecido por High-> performance container Datatypes
Todas as coleções são tipo de container
- counter: recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é
parecido com um dicionário
 - contem como chave o elemento da lista da passada por parâmetro
 - contem como valor a quantidade de ocorrências desse elemento.

"""
# Utilizando counter

from collections import Counter

# podemos utilizar qualquer iterável; foi usada uma lista como exemplo
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 34, 66, 66, 43, 34]
# Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 34: 2, 66: 2, 45: 1, 43: 1})
# muito útil para a montagem de rols em análise estatística
res = Counter(lista)

print(type(res))
print(res)
# para cada elemento da lista, o conter cria uma chave, cujo valor é a quantidade de ocorrências

# Exemplo 2
print(Counter('Geek university'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'u': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

# Exemplo 3
texto = """Wikipedia is an online free-content encyclopedia project helping to create a world in which everyone can
freely share in the sum of all knowledge. It is supported by the Wikimedia Foundation and based on a model of freely
 editable content. The name "Wikipedia" is a blending of the words wiki (a technology for creating collaborative
  websites, from the Hawaiian word wiki, meaning "quick") and encyclopedia. Wikipedia's articles provide links designed 
  to guide the user to related pages with additional information.
Wikipedia is written collaboratively by largely anonymous volunteers who write without pay. Anyone with Internet access 
can write and make changes to Wikipedia articles, except in limited cases where editing is restricted to prevent
 disruption or vandalism.
Since its creation on January 15, 2001, Wikipedia has grown into the world's largest reference website, attracting 
1.7 billion unique visitors monthly as of November 2020. It currently has more than 55 million articles in more than 
300 languages, including 6,244,361 articles in English with 146,427 active contributors in the past month.
The fundamental principles by which Wikipedia operates are the five pillars. The Wikipedia community has developed many 
policies and guidelines to improve the encyclopedia; however, it is not a formal requirement to be familiar with them 
before contributing.
Anyone is allowed to add or edit words, references, images, and other media here. What is contributed is more important 
than who contributes it. To remain, the content must be free of copyright restrictions and contentious material about 
living people. It must fit within Wikipedia's policies, including being verifiable against a published reliable source.
Editors' opinions and beliefs and unreviewed research will not remain. Contributions cannot damage Wikipedia because the 
software allows easy reversal of mistakes, and many experienced editors are watching to ensure that edits are 
improvements. Begin by simply clicking the Edit button at the top of any editable page!
Wikipedia is a live collaboration differing from paper-based reference sources in important ways. It is continually 
created and updated, with articles on new events appearing within minutes, rather than months or years. Because 
everybody can help improve it, Wikipedia has become more comprehensive than any other encyclopedia. Besides quantity, 
its contributors work on improving quality, removing or repairing misinformation, and other errors. Over time, articles 
tend to become more comprehensive and balanced. However, because anyone can click "edit" at any time and add content, 
any article may contain undetected misinformation, errors, or vandalism. Readers who are aware of this can obtain valid 
information, avoid recently added misinformation (see Wikipedia:Researching with Wikipedia), and fix the article."""

# Contagem de palavras
res = Counter(texto.split())
print(res)

# Encontrar as 5 palavras com maior ocorrência no texto
print(res.most_common(5))
