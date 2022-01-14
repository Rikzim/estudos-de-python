import time as t
x = 0
while x <= 20:
    print(x)
    x += 2
    t.sleep(0.5)
print("-"*30)
#-------------------------------------------------------------------------------

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i +=1
print("-"*30)
#-------------------------------------------------------------------------------

j = 0
while j < 6:
    j += 1
    if j == 3:
        continue
    print(j)
print("-"*30)
#------------------------------------------------------------------------------

k = 1
while k < 6:
 print(k)
 k += 1
else:
 print("k é maior ou igual a 6")
 print("-"*30)
 #-----------------------------------------------------------------------------

 nome = "Spam"
 while nome:
    print(nome)
    nome = nome[1:]

#------------------------------------------------------------------------------

print(" Adivinhe um número de 1 a 20")
op = 1
tnt = 1
my_num = 17
while op ==1:
    while tnt <= 5 and op == 1 :
        num = int(input("insira um número de 1 a 20: "))
        if num == my_num:
            print("Párabens acertoou!!")
            break
        else:
            print("Errou =/.. tente de novo ")
            tnt += 1
    else:
        print("Acabou as tentativas =/")
    op = int(input("Continuar?? - 1 \n Não continuar - 0"))



