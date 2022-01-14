import time as t
print("Completando nomes")
soma =""
for i in range(1,5):
    nome = str(input(f"{i}º Nome: "))
    soma += nome+" "


print(f"{soma}")
print("Calculando a média do seu peso nos últimos 3 meses")
soma = 0
for i in range(1,4):
    mes = int(input(f"{i}ºMês: "))
    soma += mes

media = soma/3
print(f"A média do seu peso nos últimos 3 meses é de: {media}")
tcl = input("Prima qualquer tecla para continuar...")