def potencia(base,expoente):
    resultado = base ** expoente
    return  resultado


a = int(input("Digite a base: "))

b = int(input("Digite o expoente: "))

print("O resultado final é :", potencia(a,b))

input("Prima qualquer tecla para sair.....")

#--------------------------------

def conversao_temp(temperatura):
    F = temperatura/5 *9 +32
    return F

a = int(input("Insira uma temperatura em graus Celcius: "))
print(f"{a} graus Celcius, corresponde a %.1f graus Fahrenheit" %(conversao_temp(a)))

input("Prima qualquer tecla para sair.....")


