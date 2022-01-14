
# -*- coding: latin1 -*-
import time as t
import os as o
import sys as s
o.system("color 0C")
print("-"*30)
comp1 = input ("Insira um comprimento: ")
comp2 = input ("Insira outro comprimento: ")
comp3 = input ("Insira mais um comprimento: ")

if comp1 < comp2+comp3 and comp2 < comp1+comp3 and comp3 < comp2+comp1:
    if comp1 == comp2 and comp1 == comp3:
        print("ãn?? um triangulo Equilatro")
        t.sleep(3)
        o.system("cls")
        op =int(input("fechar - 1\n : "))
        if op==1:
            t.sleep(0.5)
            s.exit
    elif comp1 != comp2 and comp2 != comp3 and comp1 != comp3:
        print("ãn??  um triangulo escaleno")
        t.sleep(3)
        o.system("cls")
        op =int(input("fechar - 1\n : "))
        if op==1:
            t.sleep(0.5)
            s.exit
    else:
        print("ãn?? um triangulo Isósceles")
        t.sleep(3)
        o.system("cls")
        op =int(input("fechar - 1\n : "))
        if op==1:
            t.sleep(0.5)
            s.exit
else:
    print("O triangulo é impossivel!")
    t.sleep(3)
    o.system("cls")
    op =int(input("fechar - 1\n : "))
    if op==1:
        t.sleep(0.5)
        s.exit













