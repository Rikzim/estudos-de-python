import time as t
print("Insira nomes e descubra o maior")
soma = 0
maximo = 0
num = int(input("Insira o número de pessoas: "))
for i in range(num):
    nome = input("Nome: ")
    idade = int(input("\t\tIdade:"))
    soma += idade
    tamanho = len(nome)
    if tamanho > maximo:
        maximo = tamanho
        maxnome = nome

print(f"Maior nome é: {maxnome}")
media = soma/num
print(f"Médias das idades é: {media}")
tcl = input("Prima qualquer tecla para continuar...")