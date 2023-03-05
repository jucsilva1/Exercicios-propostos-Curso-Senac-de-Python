a = int(0)
b = int(0)
c = int(0)
maior = int(99999)
menor = int(99999)
meio  = int(99999)
a = int(input("Digite o primeiro número: "))

b = int(input("Digite o segundo número: "))

c = int(input("Digite o terceiro número: "))

maior = a 
menor = a
meio  = a
		
if(a > b and a > c and b > c):
	maior = a
	meio = b
	menor = c
if(a > b and a > c and c > b):
	maior = a
	meio = c
	menor = b
if(b > a and b > c and a > c):
	maior = b
	meio = a
	menor = c

if(b > a and b > c and c > a):
	maior = b
	meio = c
	menor = a
if(c > a and c > b and b > a):
	maior = c
	meio = b
	menor = a
if(c > a and c > b and a > b):
	maior = c
	meio = a
	menor = b
print("O menor digitado foi {}, o maior foi {} e o do meio foi {}.".format(menor, maior, meio))

if(a == b and b == c):
    print("Os números são iguais por isso não existe maior ou menor") 