print("Menu das conversões:") #Apresenta ao utilizador um menu de conversoes
print("1 - Decimal -> Binário")
print("2 - Binário -> Decimal")
print("3 - Decimal -> Octal")
print("4 - Octal -> Hexadecimal\n")
op=int(input("Qual a operação pretendida: ")) # Pede aoutilizador aintrodução de um valor inteiro e armazena-o variavel op

if (op==1): #verifica se o valor digitado foi "1"e, caso tenha sido,executa o codigo
    decimal=int(input("Introduza o número decimal: ")) #Pede ao utilizador de um valor inteiro e armazena na variavel decimal
    print("Decimal %d = Binário %s" %(decimal,bin(decimal))) #Converte  o numero digitado para binario atraves da função bin()
    print("{0:b}".format(decimal)) #Apresenta o numero convertido em formato decimal

elif (op==2): #verifica se o valor digitado foi "2"e, caso tenha sido,executa o codigo
    binario=input("Introduza um valor binário, com o formato '0b.....': ") #Pede ao utilizador de um valor binario
    print("Binário %s = Decimal %s" %(binario,int(binario,2))) # Converte o numero digitando para inteiro atraves da função int()
    #"2" refere-se a base 2 do binario

elif (op==3): #verifica se o valor digitado foi "3"e, caso tenha sido,executa o codigo
    decimal=int(input("Introduza um valor Decimal: ")) #Pede ao utilizador de um valor binario
    print("Decimal %d = Octal %s" %(decimal,oct(decimal))) #Esta função serve para pegar o valor decimal e transforma-lo em octaldecimal
    print("{0:o}".format(decimal)) #Converte o numero digitando para inteiro atraves da função oct()
    #Apresenta o valor decimal no formato decimal
else: #Caso não seja escolhido os valores 1, 2 ou 3 o else  complementa o 4
    decimal=int(input("Introduza o número decimal: ")) #Pede ao utilizador de um valor decimal
    print("Decimal %d = Hexadecimal %s" %(decimal,hex(decimal))) # Converte o numero digitando para inteiro atraves da função hex()
    print("{0:x}".format(decimal)) #Apresenta o valor decimal no formato decimal
