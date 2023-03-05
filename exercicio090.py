num = [0]*10
num[0] = 3
cont = 0
for cont in range(0,9,1): 
    num[cont+1] = num[cont]*2
    if(num[cont] == 3 or num[cont]== 6 or num[cont] == 96):
        print(f"${num[cont]}$, ", end="")
    else:
        print(f"{num[cont]}, ", end="")