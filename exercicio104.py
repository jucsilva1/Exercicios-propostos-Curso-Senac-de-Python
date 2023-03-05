import random
num = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
contl = 0
contc = 0
maior = 0
acmedia = 0
abmedia = 0
soma = 0
for contl in range(0,4,1):
    for contc in range(0,5,1):
        num[contl][contc] = random.randint(0,10)
        if(contl == 1):
            soma = soma + num[1][contc]
media = soma/5
for contc in range(0,5,1):
    if(num[2][contc] > media ):
        acmedia = acmedia + 1
        
for contc in range(0,5,1):
    if(num[3][contc] <= media ):
        abmedia = abmedia + 1     


for contl in range(0,4,1):
    print(num[contl])

print(f"A média do grupo 1 é = {media}")
print(f"Quantidades no grupo 2 acima da média = {acmedia}")
print(f"Quantidades no grupo 3 abaixo da média = {abmedia}")

