# Controle de Fluxo
## If... Else 

# if -- se acontecer tal coisa, faça algo

# else -- senão, faça este outro algo

idade = int(input("Digite um número: "))
# int -> O input sempre converte para string, para usar como inteiro
# float -> O input sempre converte para string, para usar como inteiro

if (idade) == 25:
    print("CERTO")
else:
    print("ERRADO")

print("\n===================================================\n")

# um igual = atribuição de valores a uma variável
# dois igual == comparação
# no python não tem 3 iguais === mas em outras linguagens serve para comparar valor e tipo

"""

TIPO DE COMPARAÇÃO

== - Igual
!= - Diferente
>  - Maior
<  - Menor
>= - Maior ou igual
<= - Menor ou igual
%  - Restante da divisão

"""

idade_dois = 25
resultado = idade_dois / 5
resultado_dois = idade_dois % 2
print(resultado)
print(resultado_dois)

print("\n===================================================\n")

# Validação PAR ou ÍMPAR

# Par = números divididos por 2 com resto 0
# Ímpar = números divididos por 2 com resto 1

idade_tres = int(input("Digite um número: "))
resultado = idade_tres % 2
if resultado == 0:
    print("O número é Par")
else:
    print("O número é Ímpar")

# ou podemos usar o encurtarmento

if idade_tres % 2 == 0: 
    print("O número é Par")
else:
    print("O número é Ímpar")

print("\n===================================================\n")


numero = 25
# inteiro 5
# float 5.0 ou 5.1 

resultado_tres = numero % 6
if resultado_tres == 0:
    print("O resultado é um número inteiro")
else:
    print("O resultado é um número float")

# Para saber o tipo é melhor usar o print(type(resultado_tres))

print("\n===================================================\n")

# elif -- Mais níveis de comparações

valor = int(input("DIGITE UM VALOR: "))
if valor < 10:
    print("Valor menor que 10")
elif valor == 10:
    print("Valor igual a 10")
else:
    print("Valor maior que 10")

print("\n===================================================\n")

# Validação de variavel existente

# OBS: O nada também é um valor possível.

valor_dois = input("DIGITE UM VALOR: ")
if valor_dois:
    print("Valor existe")
else:
    print("Valor não existe")

print("\n===================================================\n")

# Validação de tipos de variáveis

var = 5 # [], , 5, 5.0, True
if type(var) == int: 
    print("int")
elif type(var) == float:
    print("float")
elif var:
    print("Var existe")
elif type(var) == bool:
    print("boolean")
elif var == True:
    print("true")
else:
    print("outro tipo")

## OBS: O fluxo para na primeira validação atendida, independente se alguma seguinte estão certas ou não, para contornar isso possível fazer do jeito abaixo, mas não é o ideal... O melhor é fazer por looping.

var = 5 # [], , 5, 5.0, True
if type(var) == int: 
    print("int")
if type(var) == float:
    print("float")
if var:
    print("Var existe")
if type(var) == bool:
    print("boolean")
if var == True:
    print("true")
else:
    print("outro tipo")