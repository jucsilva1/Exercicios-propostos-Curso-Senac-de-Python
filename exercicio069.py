numero = 0
multiplo = 1
numero = int(input("Digite um número: "))
while(numero != 1):
    print("{} X ".format(numero),end="")
    multiplo = multiplo * numero
    numero = numero - 1
print("1 = {}".format(multiplo))