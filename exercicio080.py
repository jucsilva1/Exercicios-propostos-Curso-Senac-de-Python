valor = 0
n50 = 0
n20 = 0
n10 = 0
n5  = 0
n2  = 0
n1  = 0
valor = int(input("Qual valor quer sacar? "))
while(True):
    while(valor >= 50):
        n50 = n50 + 1
        valor = valor - 50
    while(valor >= 20):
        n20 = n20 + 1
        valor = valor - 20
    while(valor >= 10):
        n10 = n10 + 1
        valor = valor - 10
    while(valor >= 5):
        n5 = n5 + 1
        valor = valor - 5
    while(valor >= 2):
        n2 = n2 + 1
        valor = valor - 2
    while(valor >= 1):
        n1 = n1 + 1
        valor = valor - 1
    if(valor < 1):
        break
print(f"Total de notas 50: {n50}.")
print(f"Total de notas 20: {n20}.")
print(f"Total de notas 10: {n10}.")
print(f"Total de notas 5: {n5}.")
print(f"Total de notas 2: {n2}.")
print(f"Total de notas 1: {n1}.")