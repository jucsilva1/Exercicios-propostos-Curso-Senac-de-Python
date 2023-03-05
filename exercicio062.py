valor = 0
cont = 0
spar = 0
simpar = 0

while(cont < 5):
    valor = int(input("Digite um número: "))
    cont = cont + 1
    if(valor %2 == 0):
        spar = spar + valor
    elif(valor %2 == 1):
        simpar = simpar + valor
print("A soma dos números ímpares é {} e a soma dos números pares {}.".format(simpar, spar))
