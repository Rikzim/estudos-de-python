import random as r

nm_rand = r.randint(1,10)
num = 0
tnt = 1
op = "s"
print("==== JOGO DO ADIVINHA ====")
print("tem 4 tentativas para adivinhar o número =)")
while tnt <= 4:
    num = int(input("Insira um número (inteiro) de 1 a 10: "))
    if num == nm_rand:
        print(f"PARABÉNS!! Acertou na {tnt}º tentativa ")
        break
    elif num > nm_rand:
        print("O número que introduziu é maior.")
        tnt +=1
    elif num < nm_rand:
        print("O número que introduziu é menor.")
        tnt +=1
if num != nm_rand:
    print("Não Acertou.... Fica para a próxima.")


