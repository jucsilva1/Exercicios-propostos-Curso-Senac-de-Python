import random;
num = 0
cont = 0

num_sort = random.randint(1,20)
print(num_sort)
while(True):
    num = int(input("Digite um número: "))
    if(num < num_sort):
        print("Você errou tente um número maior!")
        cont = cont + 1
    elif(num > num_sort):
        print("Você errou tente um número menor!")
        cont = cont + 1
    if(num == num_sort):
        print(f"Você acertou após {cont} tentativas.")
        cont = cont + 1
        break