print("------> AVALIAÇÃO ESCOLAR <------\n ")

nome = input("Insira o nome do/a aluno/a: \n")
num = int(input("Insira o número do/a aluno/a: \n"))

print("------> NOTA NOS DOMINIOS <------\n ")

print("-> Conhecimento cientifico <-")

con_c = float(input("Resultado do teste: "))

print("-> Criação de conteúdos e resolução de problemas <-")

n_ficha = float(input("Resultado da Ficha: "))

t_projet = float(input("Resultado do Trabalho de avaliação: "))

print("-> Comunicação <- ")
ob_comu = float(input("Resultado da Observação: "))

print("-> Colaboração <-")

ob_colab = float(input("Resultado da Observação: "))

#------------------------------------------------------------------------------
rst_1 = con_c*0.45
rst_2 = n_ficha*0.10
rst_3 = t_projet*0.35
rst_4 = ob_comu*0.05
rst_5 = ob_colab*0.05
rst_final = rst_1+rst_2+rst_3+rst_4+rst_5
#------------------------------------------------------------------------------

if rst_final >= 0 and rst_final < 9.5:
    print(f"O aluno/a {nome} \n Número: {num} \n Teve Insatisfatorio \n ({rst_final})")
elif rst_final >= 9.5 and rst_final < 13.5:
    print(f"O aluno/a {nome} \n Número: {num} \n Teve satisfatorio \n ({rst_final})")
elif rst_final >= 13.5 and rst_final < 15.5:
    print(f"O aluno/a {nome} \n Número: {num} \n Teve Muito satisfatorio \n ({rst_final})")
elif rst_final >= 15.5 and rst_final < 18:
    print(f"O aluno/a {nome} \n Número: {num} \n Teve Bom \n ({rst_final})")
else:
    print(f"O aluno/a {nome} \n Número: {num} \n Teve Excelente \n ({rst_final})")
