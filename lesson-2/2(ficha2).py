print("Programa verifica se tem idade para tirar/renovar carta de condução...\n ")
idade = int(input("Insira sua idade: "))

if idade >= 18 and idade <= 80:
    print("-> Está apto a Tirar/Renovar a carta.")
elif idade > 80:
    print("-> Não está apto a Tirar/Renovar a carta.")
else:
    idade_q_falta = 18 - idade
    print(f"-> Não está apto a Tirar/Renovar a carta, pois faltam-lhe {idade_q_falta} anos")

