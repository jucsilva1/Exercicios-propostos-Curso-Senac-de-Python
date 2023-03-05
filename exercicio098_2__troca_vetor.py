cont = 0
num = [0]*4
t1 = 0
t2 = 0
t3 = 0
t4 = 0
for cont in range(0,4,1):
    num[cont] = int(input("Digite um número: "))
    
t1 = num[1]
t2 = num[2]
t3 = num[3]
t4 = num[0]

num[1] = t2
num[2] = t3
num[3] = t4
num[0] = t1
print(f"{num[0]} , {num[1]}, {num[2]}, {num[3]}") 