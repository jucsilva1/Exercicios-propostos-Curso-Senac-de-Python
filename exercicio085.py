cont = 0 
num = 0
spar = 0
simpar = 0

for cont in range(0, 4, 1):
    num = int(input("Digite um número: "))
    if(num %2 == 0):
        print("É par")
        spar = spar + num
    if(num %2 == 1):
        print("É ímpar")
        simpar = simpar + num
print(f"A soma dos pares foi: {spar}")
print(f"A soma dos ímpares foi: {simpar}")