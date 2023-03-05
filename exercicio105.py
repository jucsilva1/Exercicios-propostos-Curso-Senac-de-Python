import random
num    = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
contl  = 0
contc  = 0
acerto = 0
op = str("")
for contl in range(0,4,1):
    for contc in range(0,5,1):
        num[contl][contc] = random.randint(0,10)
        if(num[contl][contc]%3 == 0):
            num[contl][contc] = 999
print(num[0])   
print(num[1]) 
print(num[2])     
print(num[3]) 

while(True):
    contl = int(input("Escolha o primeiro número para o jogo Campo Minado: "))
    contc = int(input("Escolha o segundo número para o jogo Campo Minado: "))
    op = str(input("Dejeja arriscar novamente? s ou n "))
    if(num[contl][contc] == 999):
        print("Você perdeu!")
        break
    else:
        print("Você ganhou!")
        acerto = acerto + 1
print(f"Você acertou {acerto} vez(es).")