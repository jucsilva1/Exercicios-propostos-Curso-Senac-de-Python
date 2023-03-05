par   = int(0)
impar = int(0)
spar  = int(0)
simpar = int(0)
mpar = int(0)
num1  = int(input("Digite um número: "))
num2  = int(input("Digite outro número: "))
num3  = int(input("Digite mais um número: "))
num4  = int(input("Digite mais um outro número: "))
if(num1 %2 == 0):
    mpar = num1
    par = par + 1
    spar = spar + num1
#elif(num1 %2 == 1):
    #impar = impar + 1
    #simpar = simpar + num1  

if(num2 %2 == 0):
    if(num2 > mpar):
        mpar = num2
    par = par + 1
    spar = spar + num2
#elif(num2 %2 == 1):
    #impar = impar + 1
    #simpar = simpar + num2

if(num3 %2 == 0):
    if(num3 > mpar):
        mpar = num3
    par = par + 1
    spar = spar + num3
#elif(num3 %2 == 1):
    #impar = impar + 1
    #simpar = simpar + num3

if(num4 %2 == 0):
    if(num4 > mpar):
        mpar = num4
    par = par + 1
    spar = spar + num4
#elif(num4 %2 == 1):
    #impar = impar + 1
    #simpar = simpar + num4    

print("Foram digitados {} número[s] par[es].".format(par))
print("A soma dos número[s] par[es] é {}.".format(spar))
print("O maior número par é {}.".format(mpar))