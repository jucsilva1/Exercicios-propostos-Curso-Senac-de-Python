num = 0
cont = 0

while(cont < 5):
    num = int(input("Digite um número: "))
    cont = cont + 1
    if(num %5 == 0):
        print("É multiplo de 5.")
    if(num > 10):
        print("É maior do que 10.")
    if(num < 3):
        print("É menor do que 3.")
     