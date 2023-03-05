cont = 0 
pmedio = float(0.0)
peso = float(0.0)
acima = 0
abaixo = 0
pmedio = float(input("Peso médio do brasileiro: "))
while(cont < 4):
    peso = float(input("Digite um peso: "))
    if(peso > pmedio):
        acima = acima + 1
    elif(peso <= pmedio):
        abaixo = abaixo + 1
    cont = cont + 1
print("Existe {} pessoas que está(ão) acima do peso médio e existe {} que está(ão) abaixo ou igual ao peso médio.".format(acima, abaixo))