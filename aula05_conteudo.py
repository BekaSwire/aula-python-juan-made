# CONTINUAR FALANDO SOBRE LISTAS

## .sort() - organizar a lista em ordem alfabetica ou crescente

## .sort(reverse=True) - ordena em ordem decrescente

## .reverse() - inverte a ordem

lista = [1, 2, 3]
lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

print(" -------- ")
lista = [1, 3, 2]
print(lista)
lista.reverse()
print(lista)

# Slice - Pedaço da lista [ : ]
## Dois argumentos INDEX
## [ Incluso : Excluso ]
##  [ -1 ] - ultimo lista 

lista = [1, 3, 2]
print(lista [ 0 : 2 ])

#         1    2    3    4
lista = ["a", "b", "c", "d"]
print(lista[1:3]) # só traz os do meio
print(lista[:3]) # só traz os 3 primeiros
print(lista[2:]) # só exibe os 2 últimos


# .index() - retorna a posição da lista que o valor/item está
lista = ["a", "b", "c", "d"]
print(lista.index("b"))

# NOVO MÉTODO

# .insert() - add um item a lista, mas a gente escolhe a posição que será add e anda com os outros para frente
## Entra na posição desejada e empurra os atuais para o final (fura fila)

# .append() - add um item ao final da lista

#         0    1    2
lista = ["a", "c", "d"]

#           index, valor
lista.insert(1, "b")
print(lista)

# extend() - junta valores de lista

lista1 = ["a", "b"]
lista2 = ["c", "d"]
lista3 = ["e", "f"]
lista4 = ["c", "d"]

# Junta a lista dentro da lista
lista1.append(lista2)
print(lista1)

lista2.extend(lista3)
print(lista2)

# O mesmo que criar outra lista e concatena
lista5 = lista3 + lista4
print(lista5)

# clear() - limpa os valores da lista, mas mantem a lista vazia, não exclui

lista = ["a", "b"]
lista.clear()
print(lista)

# pelo index - .pop() ou .remove = estudar

# .count() - conta quantas vezes o valor de elemento aparece na lista

lista = ["a", "c", "d", "b", "b"]
print(lista.count("b"))

# Tupla - Ordem fixa e Não pode ser alterada ()
## variável que armazena mais de um valor
var_tupla = ("a", "b", "c", "d") # não dá para editar 
print(var_tupla[1])
print(var_tupla[1:3]) # slice - exibe entre parenteses 

# entende que cada valor deve ser add em uma variável
var1, var2, var3, var4 = var_tupla 
print(var1, var2, var3, var4)

if "b" in var_tupla:
    print("existe")


# Lista - Reordenada, Alterada 
var_lista = ["a", "b", "c", "d"] 
print(var_lista[1])
print(var_lista[1:3]) # slice - exibe entre colchetes

var1 = var_lista[0]
var2 = var_lista[1]
var3 = var_lista[2]

# Saber se algum valor no index da lista
if var_lista[1] == "b":
    print("verdade")

## ----

if "b" in var_lista:
    print("existe")
else:
    print("não existe")

print(var_lista.count("b"))

# ---

# Editar uma tupla de forma não convencional (gambiarra)
## converte a tupla para lista, edita e converte de novo

var_tupla = ("a", "b", "d")

# Converto para lista para me permitir edição
print(type(var_tupla))
var = list(var_tupla)
print(type(var))

# Faço a edição desejada
var.insert(2, "c")
print(var)
print(type(var))

#Converto novamente para tupla
var_tupla = tuple(var)
print(var_tupla)
print(type(var_tupla))
