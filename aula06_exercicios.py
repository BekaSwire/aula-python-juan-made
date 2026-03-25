'''
Exercício 1:

Crie um programa que:

1- Crie um dicionário com: nome, idade e cidade

2- Exiba o nome no terminal

3- Adicione alguma profissão ao dicionário e exiba o novo dicionário

4- faça um for para exibir no terminal cada valor armazenado nas chaves do dicionário (exemplo: "nome": "juan" o juan deve ser exibido)

*

'''

print("\n=== Exercício 01 ===\n")

dicionario = {
    "nome": "Rebeca",
    "idade": "43",
    "cidade": "Rio de Janeiro",
}

print(dicionario["nome"])

dicionario["profissão"] = "QA"

print(dicionario)

for value in dicionario.values():
    print(value)

# OU

for key, value in dicionario.items():
    print(value)

'''
Exercício 2:

Crie um programa que:

1- Armazene a seguinte lista [1,2,2,3,4,4,5]

2- Remova duplicatas utilizando o set

3- Exiba a nova lista

4- Exiba no terminal o tipo da lista no momento

5- Converta de volta para lista e exiba no terminal o tipo da lista

*
'''

# Não deu tempo de ser apresentado o SET

'''
Exercício 3:

Crie um programa que:

1- Peça para o usuário digitar um nome e uma nota e armazene os 2 valores em um dicionario da seguinte forma "nome": "nota". Faça isso 3 vezes.

2- Faça um for loop para exibir os 3 nomes

3- Faça um for loop para exibir as 3 notas
'''

nome1 = input("Digite um nome1: ")
nota1 = int(input("Digite uma nota1: "))
nome2 = input("Digite um nome2: ")
nota2 = int(input("Digite uma nota2: "))
nome3 = input("Digite um nome3: ")
nota3 = int(input("Digite uma nota3: "))

dict = {
    nome1: nota1,
    nome2: nota2,
    nome3: nota3
}

for item in dict.keys():
    print(item)

for item in dict.values():
    print(item)
