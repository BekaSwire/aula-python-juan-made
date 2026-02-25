# LOOP - ciclos que acontece até que tenha uma instrução que fará ele parar


# LOOP BÁSICO
# while -- Enquanto alguma coisa acontece (condição), faça algo

num = 0
while num < 2:
    print("sucesso")
    #num = num + 1
    num += 1

# LOOP com if ... else
num = 0
while num <= 2:
    idade = int(input("Digite um número: "))
    if idade % 2 == 0:
        print("O número é PAR")
    else: 
        print("O número é ÍMPAR")
    num += 1

# LOOP COM BREAK (quando uma condição é atendida ele para no break para pausar a execução do loop... ex: usuário digitar a senha correta)
while True:
    senha = int(input("Digite sua senha: "))
    if senha == 55:
        print("Senha correta")
        break
    else: 
        print("Senha incorreta")

# # LOOP COM CONTINUE (mantém no loop, mas skip da condição, não é muito usado no WHILE)
# while True:
#     senha_dois = int(input("Digite sua senha: "))
#     if senha_dois == 55:
#         print("Senha correta")
#     else: 
#         continue
#         print("Senha incorreta")


# Exemplo prático

num = 0
while True:
    print(num)
    if num < 4:
        print("Número menor que 4")
    elif num == 5:
        print("Número igual a 5")
    elif num > 5:
        print ("Número maior que 5")
        break
    num += 1

# FOR -- para cada vez que algo acontece, faça algo

lista = [1,2,3,4]
#        0,1,2,3   lista usa o índice

range(1, 5) # usa os valores e não o índice - comece pelo 1, termine antes de 5

num = 0
# para cada valor, no intervalo de (num = 0) a 5, ele incrementa.
for i in range(num, 5):
    print("valor ", i)

# Vamos usar o FOR para somar

# Iteração com soma
soma = 0
for i in range(1, 11):
    soma += i
print(soma)

"""
Como se tivesse fazendo
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] inclui o primeiro valor e desconsidera o último valor do range
soma = soma + 1
soma = soma + 2
soma = soma + 3
...
"""

# Contar com range()
for i in range(1, 11):
    print(i)

# Index do range() -- pode ser usado para descobrir os múltiplos de um número
for i in range(0, 10, 2):
    print(i)

lista =             [0,1,2,3,4,5,6,7,8,9,10]
#index no range(1)  [0,1,2,3,4,5,6,7,8,9,10]
#index no range(2)  [0,  2,  4,  6, ,8,  10]
#index no range(3)  [0,    3,    6,    9   ]

# Inverter a contagem - do maior para o menor
for i in range(10, 0, -2):
    print(i)

# For em uma lista
frutas = ['banana', 'maçã', 'pera']
for fruta in frutas:
    print(fruta)

# Exemplo Prático misturando while com for
num_frutas = 0
frutas = []

while num_frutas < 3:
    fruta_input = input("Digite o nome de uma fruta: ")
    frutas.append(fruta_input)
    num_frutas += 1

for fruta in frutas:
    print(fruta)

# sempre que eu quiser iterar sobre uma lista devemos usar o FOR
# if dentro do for
numeros = [0, 1, 2, 3, 4, 5]
for numero in numeros:
    if numero % 2  == 0:
        print(f"O número {numero} é par")
    else:
        print(f"O número {numero} é ímpar")

# Vamos pedir para o usuário digitar números

numeros = []
while True:
    numero_input = int(input("Digite um número: "))
    numeros.append(numero_input)
    if numero_input == 0:
        break

for numero in numeros:
    if numero % 2  == 0:
        print(f"O número {numero} é par")
    else:
        print(f"O número {numero} é ímpar")

print("Código finalizado")

numeros = [0, 1, 2, 3, 4, 5]

for numero in numeros:
    var = 2
    if numero == var:
        print("O número é igual")
        break
    print("O número é diferente")


numeros = [0, 1, 2, 3, 4, 5]

for numero in numeros:
    if numero % 2  == 0:
        print("O número é par")
        continue
    else:
        print("O número é ímpar")

# OBS: Cuidado com a identação no loop, pois ele só funciona identado.