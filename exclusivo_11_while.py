valor = 0
cont = 0
spar = 0
par = 0
while(cont < 6):
    valor = int(input("Digite um valor: "))
    if(valor %2 == 0):
        par = par + 1
        spar = spar + valor
    cont = cont + 1
print(f"Foram digitados {par} par(es) e a soma é {spar}.")
    
