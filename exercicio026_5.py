cpar = int(0)
cimpar = int(0)

n1 = int(input("Digite um valor: "))
if(n1 %2 == 0):
    cpar = cpar + 1
if(n1 %2 == 1):
    cimpar = cimpar + 1
n2 = int(input("Digite outro valor: "))
if(n2 %2 == 0):
    cpar = cpar + 1
if(n2 %2 == 1):
    cimpar = cimpar + 1
n3 = int(input("Digite mais um valor: "))
if(n3 %2 == 0):
    cpar = cpar + 1
if(n3 %2 == 1):
    cimpar = cimpar + 1

print("Encotramnos {} número(s) par(es).".format(cpar))
print("Encotramnos {} número(s) ímpar(es).".format(cimpar))