"""
AULA 3

Exercício 1:

Crie um programa que:

1- Crie uma variável que armazene a lista   [1,2,3,4,5,6,7,8,9,10]

2- Exiba no terminal os 5 primeiros numeros da lista

3- Exiba no terminal os  2 últimos números da lista

"""

lista = [1,2,3,4,5,6,7,8,9,10]

#print(f"Os cinco primeiros números da lista são {lista[0:5]}")

print(f"\nOs cinco primeiros números da lista são {lista[:5]}")

#print(f"Os dois últimos números da lista são {lista[-2]} e {lista[-1]}")

print(f"\nOs dois últimos números da lista são {lista[-2:]}")

print("\n===================================================\n")

"""
Exercício 2:

Crie um programa que:

1- Crie uma variável que armazene a lista   [1,2,3,4,5,6,7,8,9,10]

2- Peça para o usuário digitar um número

3- Adicione o número que o usuário digitou a lista

4- Converta o número digitado para int

5- Exiba no terminal todos os números desta lista que são pares

"""

lista_dois = [1,2,3,4,5,6,7,8,9,10]

numero = int(input("Digite um número: "))

lista_dois.append(numero)

numeros_pares=[]
for numero in lista_dois:
    if numero % 2 == 0:
        numeros_pares.append(numero)

print(f"\nOs números pares são {numeros_pares}")

print("\n===================================================\n")


"""
Exercício 3:

Crie um programa que:

1- Crie uma variável que armazene a lista   [5, 8, 6, 1, 11, 54, 22, 0, 3]

2- Exiba a lista no terminal ordenada de forma crescente

3- Exiba a lista no terminal ordenada de forma decrescente

"""

lista_tres = [5, 8, 6, 1, 11, 54, 22, 0, 3]

lista_tres.sort()
print(f"Lista na ordem crescente {lista_tres}")

lista_tres.sort(reverse=True)
print(f"\nLista na ordem decrescente {lista_tres}")

print("\n===================================================\n")


"""
Exercício 4:

Crie um programa que:

1- Peça para o usuário digitar 5 notas

2- Armazene as 5 notas em uma lista

3- Exiba no terminal as notas ordenadas de forma crescente

4- Exiba no terminal a maior nota

5- Exiba no terminal a menor nota

6 Exiba no terminal a posição da maior nota

"""

#notas = []

# nota_1 = float(input("Digite uma nota: "))
# nota_2 = float(input("Digite uma nota: "))
# nota_3 = float(input("Digite uma nota: "))
# nota_4 = float(input("Digite uma nota: "))
# nota_5 = float(input("Digite uma nota: "))

# notas.append(nota_1)
# notas.append(nota_2)
# notas.append(nota_3)
# notas.append(nota_4)
# notas.append(nota_5)

# Usando o range
notas = []

for i in range(0, 5):
    nota = float(input(f"Digite nota {i+1}: "))
    notas.append(nota)

notas.sort()
print(f"\nAs notas informadas em ordem crescente foram {notas}")

print(f"\nA maior nota informada foi {notas[-1]}")
print(f"\nA menor nota informada foi {notas[0]}")

posicao_maior_nota = notas.index(notas[-1])
print(f"\nA posição da maior nota é {posicao_maior_nota}")