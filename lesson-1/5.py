
print("-"*30)
comp1 = input ("Insira um comprimento: ")
comp2 = input ("Insira outro comprimento: ")
comp3 = input ("Insira mais um comprimento: ")

if comp1 < comp2+comp3 and comp2 < comp1+comp3 and comp3 < comp2+comp1:
    if comp1 == comp2 and comp1 == comp3:
        print("É um triangulo Equilatro")
    elif comp1 != comp2 and comp2 != comp3 and comp1 != comp3:
        print("É um triangulo escaleno")
    else:
        print("É um triangulo Isósceles")
else:
    print("O triangulo é impossivel!")
