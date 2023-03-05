contador = 0 
while(contador < 5):
    print("Teste ")
    contador = contador + 1
    

contador2 = 0
while(contador2 < 5):
    print("Teste ",end="")
    contador2 = contador2 + 1
    
contador3 = 0
soma = 0
while(contador3 <5):
    num = int(input("Digite um número:"))
    soma = soma + num
    contador3 = contador3 + 1
print("A soma será de {} e foi contada {} vezes.".format(soma, contador3))