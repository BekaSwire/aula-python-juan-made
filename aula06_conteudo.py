# Revisão

## .extend - junta valores da lista

lista1 = [1, 2, 3] 
lista2 = [4, 5] 
lista3 =["carro", "agua", "abacate", "Abacaxi", "1", "2"]
#           0        1         2         3       4    5 
#                                       -3      -2   -1 

lista1.extend(lista2)

lista1.pop(1)
lista1.remove

# ordenar por ordem crescente ou alfabética, case sensitive
lista1.sort()
lista1.sort(reverse=True)

'''
# inverte sem mudar a ordem
lista1.extend()
'''

lista1.clear()
lista1.count("carro")

#slice (inclusivo:exclusivo)
print(lista3[0:1])

print(lista3[-2:-1])
print(lista3[:4])
print(lista3[4:-1])

#descobrir o index de um valor
print(lista3.index("agua"))

# tupla
# não pode ser modificada, editada
# não pode ser reordenada

tupla = ("carro", "agua", "abacate")
print(tupla[1])

# unpack
var1, var2, var3 = tupla

'''
O mesmo que:

var1, var2, var3 = "carro", "agua", "abacate"

var1 = tupla[0]
var2 = tupla[1]
var3 = tupla[2]
'''

# INICIO DO CONTEÚDO NOVO

'''
Tipos de Dados (4 data types no python)
1 - Lista = []
2 - Tupla = ()
3 - Dicionário = {}
4 - Set = {}()

'''

# Dicionário = {"chave":"valor"}

# Pode receber e armazenar todo tipo de dado

# com quebra de linha ou sem

# d2 = {"chave":"valor","chave2":"valor2"}

d = {
    "chave":"valor",
    "chave2":"valor2",
}

lista=["a", "b"]
#       0    1
print(lista[0])

lista[0] = "c"
print(lista)

chave = 1
print(chave)

# pode armazenar qualquer tipo valor
dicionario = {
    "chave": 1,
    "chave1": "string",
    "chave2": ["asda", "asdfsef"],
    "chave3": {"chave_interna":"valor_interno"},
    "chave4": ("valor2","valor3")
}

# a gente chama o dicionario e a chave, não o index
print(dicionario["chave2"])

# podemos alterar o valor de uma chave
dicionario["chave2"] = "nova string"

print(dicionario)

# Exibindo o valor de uma chave
print(dicionario["chave2"])

'''
var = dicionario ["chave1"]
var = "carro"
'''

# Alterando o valor de uma chave
dicionario["chave1"] = "carro"
print(dicionario["chave1"])

# Criar uma nova chave e valor no dicionario
dicionario["meunome"] = "juan"
print(dicionario["meunome"])

'''
# iterar em cada item do dicionario
for item in dicionario 
'''

# Métodos do dicionário

# .get() - alternativa para print(dicionario["chave1"]).
# Mesma coisa que o [] porém com a opção de adicionar um valor default
# pegar um valor e pode colocar uma exceção... 

print(dicionario.get("chave1"))

# Se ele não encontrar a chave, ele vai exibir um valor default no console
print(dicionario.get("chave5", "Não Existe"))

# ou 
if "chave5" not in dicionario:
    print(f"A chave5 não existe no {dicionario}")

# Exibição das chaves ou dos valores dentro do dicionário

# .keys() - chaves

print(dicionario.keys())

# .values() - valores

print(dicionario.values())

# .items() - converte o dicionário em tuplas individuais com chave e valor
# retornar uma tupla com chave e valor de todos os itens do dicionário

("chave",1)
("chave1", "string")
("chave2", ["asda", "asdfsef"])
("chave3", {"chave_interna":"valor_interno"})
("chave4", ("valor2","valor3"))

# imprimir chaves
for item in dicionario:
    print(item)

for item in dicionario.items():
    print(item)

# unpacking - iteração de cada chave e valor do dicionario
for key, value in dicionario.items():
    print(key)
    print(value)

# .pop() - remove uma chave e valor do dicionario
dicionario.pop("chave1")
print(dicionario)

# lista.remove("valor")
# lista.pop(1) -> index