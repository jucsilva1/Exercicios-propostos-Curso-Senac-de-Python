#par   = int(0)
#impar = int(0)
spar  = int(0)
simpar = int(0)
num1  = int(input("Digite um número: "))
num2  = int(input("Digite outro número: "))
num3  = int(input("Digite mais um número: "))
if(num1 %2 == 0):
    #par = par + 1
    spar = spar + num1
elif(num1 %2 == 1):
    #impar = impar + 1
    simpar = simpar + num1  

if(num2 %2 == 0):
    #par = par + 1
    spar = spar + num2
elif(num2 %2 == 1):
    #impar = impar + 1
    simpar = simpar + num2

if(num3 %2 == 0):
    #par = par + 1
    spar = spar + num3
elif(num3 %2 == 1):
    #impar = impar + 1
    simpar = simpar + num3

print("A soma dos número[s] par[es] é {}.".format(spar))
print("A soma dos número[s] ímpar[es] é {}.".format(simpar))