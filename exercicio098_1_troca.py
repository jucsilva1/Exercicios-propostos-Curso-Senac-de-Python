cont = 0
num = [12,18,11,17]
t1 = 0
t2 = 0
t3 = 0
t4 = 0
for cont in range(0,4,1):
   num[cont] = int(input("Digite um número: "))
t1 = num[0]
t2 = num[1]
t3 = num[2]
t4 = num[3]
num[0] = t2
num[1] = t3
num[2] = t4
num[3] = t1

print(f"{num[0]} , {num[1]}, {num[2]}, {num[3]}") 