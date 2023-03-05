import random
num   = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
contl = 0
contc = 0
maior = 0
menor = 99999
for contl in range(0,4,1):
    for contc in range(0,4,1):
        num[contl][contc] = random.randint(1,5)
        if(num[contl][contc] > maior):
            maior = num[contl][contc]
        if(num[contl][contc] < menor):
            menor = num[contl][contc]

for contl in range(0,4,1):
    print(num[contl])
    
print(f"O maior número digitado foi: {maior} entre os sorteados.")
print(f"O menor número digitado foi: {menor} entre os sorteados.")