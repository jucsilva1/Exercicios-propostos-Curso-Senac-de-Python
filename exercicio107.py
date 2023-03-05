import random
num    = [[0,0,0],[0,0,0],[0,0,0]]
contl  = 0
contc  = 0

numB   = [[0,0,0],[0,0,0],[0,0,0]]
contlb  = 0
contcb  = 0

res     = [[0,0,0],[0,0,0],[0,0,0]]

for contl in range(0,3,1):
    for contc in range(0,3,1):
        num[contl][contc] = random.randint(0,10)

for contl in range(0,3,1):
    for contc in range(0,3,1):
        numB[contl][contc] = num[contl][contc] * 2

for contl in range(0,3,1):
    for contc in range(0,3,1):
        res[contl][contc] = numB[contl][contc] * 2
print("Matriz Inicial")        
print(num[0])   
print(num[1]) 
print(num[2])
print("Dobro da Inicial")
print(numB[0])   
print(numB[1]) 
print(numB[2])
print("Dobro do dobro da Inicial")
print(res[0])   
print(res[1]) 
print(res[2])