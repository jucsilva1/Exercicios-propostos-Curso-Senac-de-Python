cont = int(0)
n1 = int(input("Digite um valor: "))
if(n1 > 25):
    cont = cont + 1
n2 = int(input("Digite outro valor: "))
if(n2 > 25):
    cont = cont + 1
n3 = int(input("Digite mais um valor: "))
if(n3 > 25):
    cont = cont + 1

print("Encotramnos {} números maior que 25.".format(cont))