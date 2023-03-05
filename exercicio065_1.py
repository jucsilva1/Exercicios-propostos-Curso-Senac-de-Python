num = 0 
nome = ""
cont = 0 
spar = 0
simpar = 0
midade = 0
nomev = ""
cpar = 0
cimpar = 0
while(cont < 4 ):
    num = int(input("Digite um número: "))
    nome = str(input("Digite um nome:  "))
    if(num %2 == 0):
        cpar = cpar + 1
        spar = spar + num
    if(num %2 == 1):
        cimpar = cimpar + 1
        simpar = simpar + num
    if(num > midade):
        midade = num
        nomev = nome
    cont += 1
print("A quantidade de ímpar(es) foi de {} e sua soma é {} e a quantidade de par(es) foi de {} e sua soma é {}.".format(cimpar,simpar, cpar, spar))
print("A pessoa mais velha cadastrada foi {}.".format(nomev))