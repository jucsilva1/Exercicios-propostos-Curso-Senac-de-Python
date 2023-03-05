cont  = 0
num   = [0]*3
maior = 0
menor = 0
meio  = 0
 
for cont in range(0,3,1):
   num[cont] = int(input("Digite um número: "))
   for cont in range(0,3,1):
        if(num[cont] > maior):
            maior = num[cont] 
        if(num[cont] < menor):
            menor = num[cont]
        if(num[cont] > menor and num[cont] < maior):
            meio = num[cont]
num[0] = menor
num[1] = meio
num[2] = maior
print(menor, meio, maior)

