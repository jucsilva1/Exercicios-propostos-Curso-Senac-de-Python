n1 = int(0)
n2 = int(0)
maior = int(0)
menor = int(0)
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
maior = n1
menor = n1
if(n2 > maior):
	maior = n2
if(n2 < menor):
	menor = n2 
else:
    print("Os números são iguais por isso não existe menor e maior")
    
print("O menor número digitado foi {} e o maior foi {}.".format(menor, maior,))