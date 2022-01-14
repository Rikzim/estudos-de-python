import time as t

print("==== SOMA DOS PARES e SOMA DOS ÍMPARES ====\n")

n = 10
soma_pares = 0
soma_impares = 0

while n<=200:
    if n%2 == 0:
        soma_pares = soma_pares+n
    else:
        soma_impares = soma_impares+n
    n =n+1

print(f"A soma dos números pares de 0 a 200 = {soma_pares}")
t.sleep(2)
print(f"A soma dos números ímpares de 0 a 200 = {soma_impares}")