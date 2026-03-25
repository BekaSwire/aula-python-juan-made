# Revisão de dicionários

'''
Estrutura de dados

lista = [1, 2, 3, 4]
index    0  1  2  3

tupla = (1, 2, 3, 4, 5)
--> imutável, nao reodernavel

--> unpack - a, b, c, d, e = tupla

dicionário
dict = {
    "key": "valor",
    "key2": "valor2",
    "key3": "3",
    }
pode armazenar todo tipo de dado
chave não muda, o valor sim

key .keys()
value .values()
for k, y, in dict.items()
'''

tupla = (1, 2)
a, b = tupla # unpack - para cada valor dentro da tupla, eu atribuido a uma variável

print("valor de a: ", a)
print("valor de b: ", b)


d = {
    "Salomao": 10,
    "Juan": 9
}

print(d)

print(d.keys())
print(d.items()) # tupla

for item in d:
    print(item)

for item in d.values():
    print(item)

for item in d.keys():
    print(item)

for a, b in d.items():
    print("valor de a: ", a)
    print("valor de b: ", b)


'''
Estrutura de dados
.set() --> remover valores duplicados da estrutura

O Set não permite duplicatas e não pode ser ordenado

lista = ["a", "a", "a"]
tupla = (1, 1, 1, 1)

'''

dicionario = {"chave": 1, "chave2": 1}
numeros = {1,1,1,2,2,5}
strings = {"a","b","a"} # reordena em cada execução
booleanos = {True, True, False}


transportes = ["carros", "bicicletas", "carros"]
num = set(transportes)

print(num)

set1 = {1,1,2,2,4,5}
print(set1)

set2 = {1, 2, 3, 4, 5, 5}
print(set2)

print(strings)
print(booleanos)


# Aplicando o set e alguma estrutura

lista = [1, 2, 3, 3, 4, 4, 4]
lista = set(lista)

print(type(lista))

'''
if else --> SE algo acontecer  FAÇA algo

while --> ENQUANTO algo acontece FAÇA algo

match case --> COMPARAÇÃO DIRETA

'''

x = 10

if x > 12:
    print("x maior que 12")
else:
    x+=1
    print("x menor que 12")


# IF ELSE quando é necessário usar LÓGICA

valor = int(input("Digite um valor de 1 a 5: "))

if valor <= 1:
    print("uma coisa")
elif valor ==2:
    print("duas coisas")
elif valor ==3:
    print("tres coisas")
elif valor ==4:
    print("quatro coisas")
elif valor ==5:
    print("cinco coisas")

# MATCH CASE quando é necessário comparar VALORES EXATOS

match valor:
    case 1:
        print("uma coisa")
    case 2:
        print("duas coisas")
    case 3:
        print("tres coisas")
    case 4:
        print("quatro coisas")
    case 5:
        print("cinco coisas")
    case _:
        print("valor incorreto")

letra = input("Digite uma letra: ")

if letra == "a":
    print("A")
elif letra == "b":
    print("B")
else:
    print("Letra inexistente")



while True:
    valor = input("Digite uma letra: ")
    match valor:
        case "a":
            print("Senha correta")
            break
        case _:
            print("Senha incorreta")

'''
while valor != "a":
    valor = input("Digite uma letra: ")
        valor == "a":
        break
        print("Senha incorreta")
'''

letra = input("Digite uma letra: ")

while valor != "b":
    print("valor diferente de B")
    valor = "b"
    print("valor igual a b")


'''
sum() - Soma
max() - Maior valor
min() - Menor valor
'''

valores = (1, 2, 3, 7, 5)
print(sum(valores))
print(max(valores))
print(min(valores))

soma = sum(valores)
print(soma)
print(f"A soma dos valores é {soma}")

valor_maximo = max(valores)
print(f"O valor máximo é {valor_maximo}")

valor_minimo = min(valores)
print(f"O valor mímimo é {valor_minimo}")