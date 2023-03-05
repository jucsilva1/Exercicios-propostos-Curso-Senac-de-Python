valor = 0
cont  = 0
total = 0

while (cont != 3):
    valor = int(input("Digite um valor: "))
    cont = cont + 1
    total = total + valor
print("Foram digitados {} valores.".format(cont))
print("A soma destes {} valores é {}.".format(cont, total))
