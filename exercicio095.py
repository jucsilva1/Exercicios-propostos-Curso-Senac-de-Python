import random

cont = 0
print("Números aleatórios de 0 a 60: ")
for cont in range(1, 7):
    num = random.randint(0,60)
    print(f"=> {num}")