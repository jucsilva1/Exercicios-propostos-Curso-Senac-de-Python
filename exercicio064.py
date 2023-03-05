valor = 0
cont = 0
m3 = 0
m5 = 0
while(cont < 7):
    valor = int(input("Digite um número: "))
    cont = cont + 1
    if(valor %3 == 0):
        m3 = m3 + 1
    if(valor %5 == 0):
        m5 = m5 + 1
      
print("Foram identificados {} números múltiplos de 5 e {} que são múltiplos de 3.".format(m5, m3))