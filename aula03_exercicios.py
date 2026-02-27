print("\n===================================================\n")

print("EXERCÍCIOS AULA 3")

print("\n===================================================\n")


"""

AULA 3

Exercício 1:

Crie um programa que:

1- Crie uma variável que armazene a seguinte lista:  [10, 15, 22, 33, 40]

2- Utilize um for loop para iterar sobre cada item desta lista

3- Printar no terminal, quais itens da lista são pares

Exemplo de exibição: 
10 é par
22 é par
...

"""

print("Execício 1\n")

numeros = [10, 15, 22, 33, 40]
for numero in numeros:
    if numero % 2 == 0:
        print(f"{numero} é par")

print("\n===================================================\n")

"""

Exercício 2:

Crie um programa que:

1- Crie um loop que peça para o usuário digitar qualquer coisa ou digitar sair caso queira fechar o programa

2- Printar no terminal o que o usuário digitou

3- Caso o usuário digite sair o programa é finalizado

Exemplo de exibição:  

"Você digitou sair"

"""

print("Execício 2\n")

while True:
    digite = input("Digite qualquer coisa ou digite sair caso queira fechar o programa: ") # não precisa converter para string, pq o input já é uma string
    if digite == "sair":
        print(f"Você digitou {digite} e o programa será fechado")
        break
    else: 
        print(f"Você digitou {digite} e o programa vai continuar")

print("\n===================================================\n")