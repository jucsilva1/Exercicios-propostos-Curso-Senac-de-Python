import random
num = 0 
num_sort =0 
op = 0
vit = 0
derr =0 
num_sort = random.randint(1,9)
while(True):
    op= int(input("Escreva se deseja 1- Par ou 2- Ímpar: "))
    soma = num_sort + num
    if(op == 1 and soma %2 == 0):
        print("Você venceu!")
        vit = vit + 1
        break
    elif(op == 2 and soma %2 == 1):
        print("Você venceu!")
        vit = vit + 1
        break
    else:
        print("Você perdeu!")
        derr = derr + 1
print(f"Você teve {vit} vitória(s).")
print(f"Você teve {derr} derrota(s).")