import random
num = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
contl = 0
contc = 0
maior = 0
simpar = 0
spar = int(0)
for contl in range(0,3,1):
    for contc in range(0,3,1):
        num[contl][contc] = random.randint(0,10)
        if(num[contl][contc] > maior ):
            maior = num[contl][contc]
        if(num[contl][contc]%2 == 0):
            spar = spar + num[contl][contc]
        if(num[contl][contc]%2 == 1):
            simpar = simpar + num[contl][contc]

for contl in range(0,3,1):
    print(num[contl])
    
print(f"O maior valor é = {maior}")
print(f"A soma dos pares = {spar}")
print(f"A Soma dos ímpares = {simpar}")
