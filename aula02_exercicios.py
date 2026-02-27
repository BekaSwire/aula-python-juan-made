
print("\n===================================================\n")

print("EXERCÍCIOS AULA 2")

print("\n===================================================\n")

"""

AULA 2

Exercício 1:

Crie um programa que:

1- Peça um número para o usuário.

2- Converta o número para Inteiro.

3- Exiba no terminal se o número é par ou ímpar

Exemplo de exibição: “O número que você digitou é PAR"

"""

print("Execício 1\n")

numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print(f"O número {numero} é PAR")
else:
    print(f"O número {numero} é ÍMPAR")

print("\n===================================================\n")


"""
Exercício 2:

Crie um programa que:

1- Peça para o usuário digitar uma idade

2- Converta o número para Inteiro

3-  Exiba no terminal se a idade é de uma criança, Adolescente, Adulto ou Idoso.
- Crianças devem ter menos de 12 anos

- Adolescentes devem ter de 12 a 18 anos

- Adultos devem ter de 18 a 60 anos

- Idosos devem ter mais de 60 anos

Exemplo de exibição:  "A idade digitada é de um Adolescente!"

"""

print("EXERCÍCIO 2\n")

idade = int(input("Digite uma idade: "))

if idade < 12:
    print(f"Uma pessoa com {idade} anos é considerada uma criança")
elif idade < 18:
    print(f"Uma pessoa com {idade} anos é considerada uma pessoa adolescente")
elif idade < 60:
    print(f"Uma pessoa com {idade} anos é considerada uma pessoa adulta")
else:
    print(f"Uma pessoa com {idade} anos é considerada uma pessoa idosa")


print("\n===================================================\n")


print("EXERCÍCIO 2 - outra maneira de escrever, com AND\n")

idade_dois = int(input("Digite uma idade: "))

if idade_dois < 12:
    print(f"Uma pessoa com {idade_dois} anos é considerada uma criança")
elif idade_dois >= 12 and idade_dois < 18:
    print(f"Uma pessoa com {idade_dois} anos é considerada uma pessoa adolescente")
elif idade_dois >=18 and idade_dois < 60:
    print(f"Uma pessoa com {idade_dois} anos é considerada uma pessoa adulta")
else:
    print(f"Uma pessoa com {idade_dois} anos é considerada uma pessoa idosa")

print("\n===================================================\n")
