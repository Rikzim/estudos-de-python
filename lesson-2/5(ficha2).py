print("-------- CALCULADOR DE IMC --------\n")
peso_c = float(input("Insira o teu peso: "))
alt_c = float(input("Insira a tua altura: "))
IMC = peso_c / (alt_c*alt_c)

if IMC <16:
    print("O teu IMC é de Magreza grave")

elif IMC > 16 and IMC < 17:
    print("O teu IMC é de Magreza moderada")

elif IMC >= 17.1 and IMC < 18.5:
    print("O teu IMC é de Magreza leve")

elif IMC >= 18.51 and IMC < 25:
    print("O teu IMC é de Magreza leve")

elif IMC >= 25.1 and IMC < 30:
    print("O teu IMC é de Sobrepeso")

elif IMC >= 30.1 and IMC < 35:
    print("O teu IMC é de Obesidade Grau I")

elif IMC >= 35.1 and IMC < 40:
    print("O teu IMC é de Obesidade Grau II (severa)")

else:
    print("O teu IMC é de Obesidade Grau III (mórbida)")

print("-"*35)





