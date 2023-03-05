num = int(input("Digite um número:"))
if(num == 0):
    print("É zero.")
elif(num < 0):
    print("É negativo.")
elif(num %2 == 0):
    print("É par.")
elif(num %2 == 1):
    print("É ímpar.")