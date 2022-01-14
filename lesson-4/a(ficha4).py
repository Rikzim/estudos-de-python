import time as t
print("Aplicação que descomplica a tabuada\n","-"*35)

tab = int(input("Qual é a tabuada que considera mais difícil?: "))
print("Vamos, então, a isso... bem devagar..")

for i in range(1,11):
    print(f"{tab} * {i} =",tab*i)
    t.sleep(2)

tcl = input("Prima qualquer tecla para continuar...")