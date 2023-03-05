import random 

mega1 = random.randint(1,60)
mega2 = random.randint(1,60)
mega3 = random.randint(1,60)
mega4 = random.randint(1,60)
mega5 = random.randint(1,60)
mega6 = random.randint(1,60)

num1 = int(input("Digite 1° número: "))
num2 = int(input("Digite 2° número: "))
num3 = int(input("Digite 3° número: "))
num4 = int(input("Digite 4° número: "))
num5 = int(input("Digite 5° número: "))
num6 = int(input("Digite 6° número: "))

if(num1 == mega1):
    print("Você acertou o 1° número sorteado que foi: {}.".format(mega1))
else:
    print("Errou! {}.".format(num1))
    
if(num2 == mega2):
    print("Você acertou o 2° número sorteado que foi: {}.".format(mega1))
else:
   print("Errou! {}.".format(num2))

if(num3 == mega3):
    print("Você acertou o 3° número sorteado que foi: {}.".format(mega1))
else:
   print("Errou! {}.".format(num3))

if(num4 == mega4):
    print("Você acertou o 4° número sorteado que foi: {}.".format(mega1))
else:
    print("Errou! {}.".format(num4))

if(num5 == mega5):
    print("Você acertou o 5° número sorteado que foi: {}.".format(mega1))
else:
    print("Errou! {}.".format(num5))
    
if(num6 == mega6):
    print("Você acertou o 6° número sorteado que foi: {}.".format(mega1))
else:
    print("Errou! {}.".format(num6))
    