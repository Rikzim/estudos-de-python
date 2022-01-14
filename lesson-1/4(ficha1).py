
import time as t
print("-----------------------------")
print("Fim -1 \nInserir -2 \nConsultar - 3")
op = int(input("Insira uma opção: "))
if op == 1:
    print("Você inseriu a opção Fim")
elif op == 2:
    print("Você inseriu a opção Inserir")
elif op == 3:
    print("Você inseriu a opção Consultar")
else:
    print("Opção Inválida!!")
    t.sleep(4)
