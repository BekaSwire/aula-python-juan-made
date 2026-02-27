# Funções e Operadores básicos

## nome da função seguido por parenteses
print("O print exibe no termina o que está entre parenteses")
print(5+5-8*5/7)

# Variáveis e Tipos de variáveis

nome_variavel = 5+5 #tipo inteiro
print(nome_variavel)

#Tipos de variáveis

tipo_inteiro = 1 #1, 2, 3, 4, 5, 10, 20, 50

tipo_float = 1.1 #1.1, 2.0, 3.10, 50.55555

tipo_string = "entre aspas duplas ou simples" #qualquer texto em aspas

tipo_boolean = True #True ou False

tipo_lista = ["texto", 5, 5.5] #usa o colchetes [], pode armazenar qualquer tipo

variavel_s = "texto"

#print(nome_variavel + variavel_s) #tipos diferente vai dar ruim

print(type(nome_variavel)) #descobrir o tipo da variável

idade = 10
sobremesa = "chocolate"

print(type(idade))

print(f"Eu tenho {idade} anos e gosto de {sobremesa}") #fstring = concatena
print("Eu tenho ", idade, "anos") #não é muito usual

# Listas

## Manipulação de listas

lista_string = ["a", "b", "c"] #começa na posição 0 - 1o campo
#                0    1    2

#índice da lista => posição
# 0 => a
# 1 => b
# 2 => c

lista_numeros = [1, 2, 3]
#               0  1  2

#índice da lista => posição
# 0 => 1
# 1 => 2
# 2 => 3

print(lista_string[0]) #passar índice do item lista

# append => adicionar um valor a algo existente

lista_string.append(lista_numeros)
lista_string.append(["a", "b", "c"])

nova_lista =  ["a", "b", "c", [1, 2, 3], ["a", "b", "c"]]
#               0    1    2    3  3  3     4    4    4

print(nova_lista[3][1])

# remove => remover itens, remove pelo valor e não pelo indice.

lista_string_dois = ["a", "b", "c"] 
lista_string_dois.append("d")

print(lista_string_dois)

lista_string_dois.remove("d")

print(lista_string_dois)

nova_lista.remove([1, 2, 3])

nova_lista.remove(nova_lista[3]) # ou => nova_lista.remove([1, 2, 3])

# input => entrada de valor, recebe a resposta do usuário com o tipo string e precisa ser armazenada numa variável

idade_usuario = input("Digite sua idade: ")
print(f"A sua idade é: {idade_usuario}")

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

nome_sobrenome = [] #criar uma lista vazia
nome_sobrenome.append(nome) #índice 0
nome_sobrenome.append(sobrenome) #índice 1

print(nome_sobrenome[0])
print(nome_sobrenome[1])
print(nome_sobrenome)
