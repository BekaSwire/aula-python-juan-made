# REVISÃO

# for - iteração sobre cada valor indice da lista 
# alteração, busca, edição, 

lista = [1, 2, 3]

for valor in lista:
    valor_novo = valor*2
    print(valor_novo)

# WHILE -- Enquanto alguma coisa acontece (condição), faça algo
# FOR -- para cada vez que algo acontece, faça algo

print("\n===================================================\n")

i = 0

while i < 2:
    print(f"i é {i}")
    i += 1

print("\n===================================================\n")

# conversão do input que é uma string por padrão
valor = int(input("digite um numero: "))
print(valor)
print(type(valor))

print("\n===================================================\n")

# LISTA - Métodos

# sort() - ordenar números por ordem crescente, ordem alfabética de string
lista_num = [5, 1, 8, 3, 2] 
lista_p = [ "camelo", "carro", "abacate", "mansão", "jato"]

lista_num.sort()
print(lista_num)

lista_p.sort()
print(lista_p)

print("\n===================================================\n")

# ordenar em ordem decrescente
lista_num.sort(reverse=True)
print(lista_num)

lista_p.sort(reverse=True)
print(lista_p)

# sorted - retorna o valor da lista ordenada de forma mais direta

print(sorted(lista_p))
lista_p_ordenada = sorted(lista_p)

# Problemas comuns 

# Sorted é case sensitive
print("\nSorted é case sensitive")

lista_p_maisculas_minusculas_numeros = [ "Ator", "Bala", "camelo", "carro", "abacate", "mansão", "jato", "1", "2"]
print(sorted(lista_p_maisculas_minusculas_numeros))

print("\n===================================================\n")

# .reverse() - Inverte a ordem dos índices lista, sem ordenar
lista_diferente = [2, 5, 3, 10]
lista_diferente.reverse()
print(lista_diferente)

print("\n===================================================\n")

# Slice [ : ] - Cortar partes especificas da lista, fatia da lista, baseada nos índices da lista
lista = ["a", "b", "c", "d", "e"]
#         0,   1,   2,   3    4

# o primeiro é inclusivo e o último é exclusivo
print(lista[1:3])

# Tira o primeiro valor "a" --> ["b", "c", "d"]
print(lista[1:])

# Tira o indice 3 "d" --> ["a", "b", "c"] 
print(lista[:3])

# Pegar o último número da lista
print(lista[-1])

# Traz valores de indices em intervalos => no caso, de 2 em 2
print(lista[::2])

# Inverte os valores trazidos pelo intervalo
print(lista[::-2])

print("\n===================================================\n")

# index()
frutas = ["banana", "maça", "pera"]
#             0   ,   1   ,   2

posicao = frutas.index("maça")
print(posicao)

#se tiver valores duplicados na lista, ele traz a posição da primeira ocorrencia