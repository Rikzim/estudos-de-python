#
num = int(input("Introduza um valor: "))
num1 = int(input("Introduza outro valor: "))
if num>num1:
    print("O", num, "é maior que ", num1)
elif num1>num:
    print("O", num1, "é maior que ", num)
else:
    print("Os números são iguais")
