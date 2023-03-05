cont = 1
s5 = 0
while(cont <= 500):
    if(cont %5 == 0 and cont %2 == 1):
        s5 = s5 + cont
    cont = cont + 1
print(f"A soma dos números ímpares de 1 a 500 é {s5}.")
    