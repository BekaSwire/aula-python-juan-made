print("\n===================================================\n")

print("EXERCÍCIOS AULA 5")

print("\n===================================================\n")

"""

AULA 5

Exercício 1:

Crie um programa que:

1- Crie uma variável que armazene a lista   ['arroz', 'carro', 'escola', 'abacate', 'feijão', 'arroz']

2- Conte quantas vezes arroz está na lista e exiba no terminal

3- Retire o último 'arroz' da lista

4- Exiba a nova lista

"""

print("Execício 1\n")

lista = ['arroz', 'carro', 'escola', 'abacate', 'feijão', 'arroz']

vezes_arroz = lista.count('arroz')

print(f"Arroz aparece {vezes_arroz} na lista")

lista2 = lista[:5]

print(f"A nova lista é {lista2}")


# para usar o remove
print("\n-->> Usando .remove(), usar o reverse() e remover corretamente o último arroz")
lista.reverse()
lista.remove('arroz')
lista.reverse()
print(f"A nova lista é {lista}")

# slice negativo
print("\n-->> Usando o slice negativo")

lista_slice = ['arroz', 'carro', 'escola', 'abacate', 'feijão', 'arroz']

lista3 = lista_slice[:-1]

print(f"A nova lista é {lista3}")

print("\n===================================================\n")

"""

Exercício 2:

Crie um programa que:

1- Crie uma variável que armazene a lista [1,2,3]

2- Crie uma segunda variável que armazene esta lista  [4,5,6]

3- Faça a primeira lista armazenar também os valores da segunda lista

4- Exiba a primeira lista atualizada

5- Limpe toda a primeira lista e a exiba no terminal

"""

print("Execício 2\n")

lista = [1,2,3]
lista_dois = [4,5,6]

lista.extend(lista_dois)
print(f"A lista atualizada é {lista}")

lista.clear()
print(f"A lista limpa é {lista}")

print("\n===================================================\n")

"""

Exercício 3:

Crie um programa que:

1- Crie uma tupla que armazene 5 nomes

2- Exiba no terminal o segundo nome

3- Exiba no terminal os 3 primeiros nomes

4- Verifique se o nome Mariana está na lista

"""

print("Execício 3\n")

nomes_tupla = ('Rebeca', 'Karla', 'Larissa', 'Sâmilly', 'Rosana')

print(f"O segundo nome da tupla é {nomes_tupla[1]}")
print(f"O três primeiros nomes da tupla são {nomes_tupla[:3]}")

if 'Mariana' in nomes_tupla:
    print("Mariana está na tupla")
else:
    print("Mariana não está na tupla")

print("\n===================================================\n")

"""
Exercício 4:

Crie um programa que:

1- Armazene a seguinte tupla dados = ("Carlos", 30, "Brasil")

2- Faça o unpack desta tupla em 1 linha, armazenando os 3 valores nas variáveis, nome, idade, nacionalidade

3- Exiba no terminal o valor das variáveis nome, idade e nacionalidade

4- Adicione 'Programador' no índice 1 da tupla 'dados'

5- Exiba no terminal a nova tupla 'dados'

"""

print("Execício 4\n")

dados_tupla = ("Carlos", 30, "Brasil")

nome, idade, nacionalidade = dados_tupla

print(f"Nome: {nome} \nIdade: {idade} \nNacionalidade: {nacionalidade}")

dados_var = list(dados_tupla)
dados_var.insert(1, 'Programador')

dados_tupla=tuple(dados_var)

print(f"A nova tupla de dados é {dados_tupla}")

print("\n===================================================\n")