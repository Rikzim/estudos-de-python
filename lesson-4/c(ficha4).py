import time as t
import os as o
o.system('color F2')
print("A média da turma, no 1º módulo de PSI")
op = int(input("insira a quantidade de alunos que prentende ver a nota: "))
t.sleep(2)
nota = 1
for i in range(1,op+1):
    print(f"Aluno nº {i} : ")
    print("-"*25)
    nome = input("Nome? ")
    nota = int(input("Nota do 1º módulo de PSI: "))
    while nota < 0 or nota > 20:
        print("insira uma nota valida")
        nota = int(input("Nota do 1º módulo de PSI: "))
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