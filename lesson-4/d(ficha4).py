import time as t
print("Insira 3 nomes e descubra o maior")
soma = 0
maximo = 0
for i in range(3):
    nome = input("Nome: ")
    idade = int(input("\t\tIdade:"))
    soma += idade
    tamanho = len(nome)
    if tamanho > maximo:
        maximo = tamanho
        maxnome = nome

print(f"Maior nome é: {maxnome}")

print(f"Médias das idades é: {soma/3}")
tcl = input("Prima qualquer tecla para continuar...")
