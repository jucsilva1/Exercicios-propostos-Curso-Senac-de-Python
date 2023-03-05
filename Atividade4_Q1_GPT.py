import random

def main():
    # Sorteando os números aleatórios
   
    num = [random.randint(1, 100) 
    for i in range(4)]
    maior = 0
    menor = 9999

    # Encontrando o maior e o menor número
    if(num[0] > maior):
        maior = num[0]
    if(num[1] > maior):
        maior = num[1]
    if(num[2] > maior):
        maior = num[2]
    if(num[3] > maior):
        maior = num[3]
        
    if(num[0] < menor):
        menor = num[0]
    if(num[1] < menor):
        menor = num[1]
    if(num[2] < menor):
        menor = num[2]
    if(num[3] < menor):
        menor = num[3]     
   
    # Imprimindo o resultado
    print("Números sorteados:", num)
    print("Maior número:", maior)
    print("Menor número:", menor)
    
main()
