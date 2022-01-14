def numero_par(valor):
    valor = valor%2
    if valor == 0:
        return True
    else:
        return False
op = "S"
while op in ("Sim","sim","s","S"):
    a= int(input("Digite um valor para verificar se é par: "))

    print(numero_par(a))

    op = input("Deseja repetir ?: ")
    if op == "Sim" or "sim" or "S" or "s":
        continue

    else:
        break
