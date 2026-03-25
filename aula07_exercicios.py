'''
Exercícios de fixação - Aula 7

Exercício 1:

Crie um programa que:

1- Armazene a seguinte lista [1,2,2,3,4,4,5]

2- Remova duplicatas utilizando o set

3- Exiba a nova lista

4- Exiba no terminal o tipo da lista no momento

5- Converta de volta para lista e exiba no terminal o tipo da variável

*

'''

print("\n=== Exercício 01 ===\n")

lista = [1,2,2,3,4,4,5]

set_lista = set(lista)

print(set_lista)

print(type(set_lista))

lista_filtrada = list(set_lista)

print(type(lista_filtrada))

'''
Exercício 2:

Crie um programa que:

1- Faça um for loop que peça para o usuário digitar um nome e uma nota e armazene os 2 valores em um dicionário, o nome deve ser a key e a nota deve ser o valor
("nome": "nota"). 

2- Exiba no terminal a maior nota

3- Exiba no terminal a média das notas

'''

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

print(dict)
'''


# OU MELHOR

print("\n=== Exercício 02 ===\n")

dict = {}

for i in range(3):
    nome = input("Digite um nome: ")
    nota = float(input("Digite uma nota: "))
    dict[nome] = nota

print(dict)

nota_maxima = (max(dict.values()))
print(f"A nota máxima da turma foi {nota_maxima}")

nota_media = (sum(dict.values())/len(dict))
print(f"A nota média da turma foi {nota_media}")

'''
Exercício 3:

Crie um programa que utilizando o match case:

1- Ao ser executado exiba no terminal:
Selecione o menu desejado:
1 - Adicionar número
2 - Ver lista
3 - Sair

2- Se o usuário digitar 1 exiba no terminal:
Digite um número: 
Quando o usuário digitar o número, adicione este número a uma lista

3- Se o usuário digitar 2 exiba no terminal: 
Exiba no terminal a lista de números

4-Se o usuário digitar 3 exiba no terminal:
Você digitou "sair" fechando programa
E depois finalize o programa


'''

print("\n=== Exercício 03 ===\n")

print("Selecione o menu desejado:\n1 - Adicionar número\n2 - Ver lista\n3 - Sair\n")

lista = []

while True:
    opcao_escolhida = (int(input("Qual a opção desejada: ")))
    print(f"Você optou por {opcao_escolhida}")
    match opcao_escolhida:
        case 1:
            num = int(input("Digite um número: "))
            lista.append(num)
        case 2:
            print(f"A lista de numeros atual é {lista}")
        case 3:
            print("O programa será fechado")
            break
        case _:
            print("Opção Inválida")



