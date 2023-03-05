import random
num = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
contl = 0
contc = 0
soma = int(0)
for contl in range(0,4,1):
    for contc in range(0,4,1):
        num[contl][contc] = random.randint(0,10)
        if(contl == 2):
            soma = soma + num[contl][contc]

for contl in range(0,4,1):
    print(num[contl])
    
print(f"Soma do grupo 2 = {soma}")
    
