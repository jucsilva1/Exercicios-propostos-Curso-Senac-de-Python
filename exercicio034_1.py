par  = int(0)
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite mais um número: "))
if(num1 %2 == 0):
    par = par + 1
if(num2 %2 == 0):
    par = par + 1
if(num3 %2 == 0):
    par = par + 1

print("Foram encotrados {} número[s] par[es].".format(par))