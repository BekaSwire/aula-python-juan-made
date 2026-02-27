print("\n===================================================\n")

print("EXERCÍCIOS AULA 1")

print("\n===================================================\n")

print("Execício 1\n")


"""

AULA 1

Exercício 1:

Crie um programa que:

1- Peça o nome do usuário

2- Peça a idade.

3- Mostre a mensagem:

Exemplo de exibição: "Olá Juan, você tem 27 anos!"

"""

nome = input("Digite seu nome: ")

idade = int(input("Digite a sua idade: "))

print(f"Olá {nome}, você tem {idade} anos!")

print("\n===================================================\n")

"""

Exercício 2:

Crie um programa que:

1- Peça para o usuário digitar 3 cores. (pode ser em 1 ou 3 perguntas)

2- Exiba a 2 cor que ele digitou:

Exemplo de exibição: Sua segunda cor favorita é: Azul

"""

print("Execício 2\n")

cor_um = input("Digite sua primeira cor favorita: ")
cor_dois = input("Digite sua segunda cor favorita: ")
cor_tres = input("Digite sua terceira cor favorita: ")

print(f"Sua segunda cor favorita é: {cor_dois}")

print("\n===================================================\n")

"""

Exercício 3:

Crie um programa que:

1- Peça o nome e idade do usuário.

2- Peça três comidas favoritas (usando input() três vezes).

3- Armazene as comidas em uma lista.

4- Mostre a mensagem: "Olá [nome]! Você tem [idade] anos e suas comidas favoritas são [lista]." (pode exibir a lista completa sem tratamentos)

Exemplo de exibição: Olá Mariana! Você tem 25 anos e suas comidas favoritas são ['pizza', 'sushi', 'macarrão'].

"""

print("Execício 3\n")

nome_usuario = input("Digite seu nome: ")

idade_usuario = int(input("Digite a sua idade: "))

comidas_favoritas = []

comida_um = input("Digite sua primeira comida favorita: ")
comida_dois = input("Digite sua segunda comida favorita: ")
comida_tres = input("Digite sua terceira comida favorita: ")

comidas_favoritas.append(comida_um)
comidas_favoritas.append(comida_dois)
comidas_favoritas.append(comida_tres)

print(f"Olá {nome_usuario}! Você tem {idade} anos e suas comidas favoritas são {comidas_favoritas}.")

print("\n===================================================\n")