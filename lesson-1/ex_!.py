qts_notas = 0
soma_notas = 0
nota = 1
while (nota != 0 ):
    nota = int(input ("Insira uma nota (1,2,10..)"))
    qts_notas+=1
    soma_notas = soma_notas+nota

media = soma_notas/qts_notas
print(f"Inseriu {qts_notas} notas ")
print(f"Media das notas = %.4f" %(media))