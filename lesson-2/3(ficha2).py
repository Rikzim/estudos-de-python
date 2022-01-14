

print("------- BANCO DINHEIROCERTO ------\n")

sal_c = float(input("Insira o valor do seu salario: "))
mnt_c = float(input("Insira o montante de emprestímo a pedir: "))

if mnt_c <= sal_c*5:
    print(" --> Financiamento concedido")
    print(f"O ciente tem um salario de {sal_c} Euros e pretende um enprestimo de {mnt_c} Euros")
    print("Obrigado por nos consultar ")
else:
    print(" --> Financiamento Negado")
    print(f"O ciente tem um salario de {sal_c} Euros e pretende um enprestimo de {mnt_c} Euros")
    print("Obrigado por nos consultar ")



