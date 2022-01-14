print("==== CÁLCULO DO DOBRO E DO TRIPLO ====\n")

num1 = 1


while num1 != 0:
    num1 = int(input("Insira um número inteiro (0 para terminar): "))
    dobro = num1*2
    triplo = num1*3
    if num1 != 0:
        print(f"Dobro = {dobro}")
        print(f"Triplo = {triplo}")


