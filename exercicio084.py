num = 0
cont = 0
prod = 0
num = int(input("Digite o número da tabuada: "))
print(f"A tabuada de {num} é: ")
for cont in range(1, 11, 1):
    prod = num * cont
    print(f"{num} X {cont} = {prod}")