import time as t
import os as o

print("A média da turma, no 1º módulo de PSI")
o.system('color F2')
t.sleep(2)
for i in range(1,4):
    print(f"Aluno nº {i} : ")
    print("-"*25)
    nome = input("\t\tNome? ")
    nota = int(input("\t\tNota do 1º módulo de PSI: "))
    print("-"*25)
print("A média da turma, no 1º módulo de PSI é de")
print("\tAguarde...")
t.sleep(5)
print("\tAguarde mais um pouco...")
t.sleep(5)
print("\tAgora, sim! A resposta é...")
t.sleep(10)
print("Lamento mas, \ncumpre -me informa-lo que terá que esperar por uma das proxima aulas.")
tcl = input("Prima qualquer tecla para continuar...")