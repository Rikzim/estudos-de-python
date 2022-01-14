import random as r
import time as t
def boss_v():
    print("1 - Espada de fogo \n2 - Espada e gelo \n3 - Espada de materia negra")
    esp = int(input("Escolha sua espada: "))
    hp = 300
    t.sleep(2)
    while hp >= 0:
        if esp == 1:
            op = int(input(f"Voce tem a espada {esp}"))
            if op == 1:
                r1 = r.randint(30,100)
                t.sleep(5)
            elif op == 2 :
                r1 = r.randint(30,200)
                t.sleep(2)
            elif op == 3:
                r1 = r.randint(30,300)
                t.sleep(1.5)
        if esp == 2:
            op = int(input(f"Voce tem a espada {esp}"))
            if op == 1:
                r1 = r.randint(30,100)
                t.sleep(5)
            elif op == 2 :
                r1 = r.randint(30,200)
                t.sleep(2)
            elif op == 3:
                r1 = r.randint(30,300)
                t.sleep(1.5)
        if esp == 3:
            op = int(input(f"Voce tem a espada {esp}"))
            if op == 1:
                r1 = r.randint(30,100)
                t.sleep(5)
            elif op == 2 :
                r1 = r.randint(30,200)
                t.sleep(2)
            elif op == 3:
                r1 = r.randint(30,300)
                t.sleep(1.5)
        hp = hp-r1
        print(hp)
    print("boss derrotado!!")



boss_v()



