cont = 0
num =[0]*4
cont9 = 0
for cont in range(0,4,1):
    num[cont] = int(input("Digite um valor: "))
    if(num[cont] == 9):
        cont9 = cont9 + 1
print(f"O número 9 apareceu {cont9} vez(es).")