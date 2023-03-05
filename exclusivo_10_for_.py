cont = 1
containt = 1

num = int(input("Digite um número: "))
while(cont < num):
    if(num % cont == 0):
        containt = containt + 1
    cont = cont + 1
print(f"Foram encontrados {containt} divisões inteiras.")
if(containt == 2):
    print("O número é primo")
else:
    print("O número não é primo")