maior = int(0)
soma  = int(0)
n1 = int(0)
n2 = int(0)
n3 = int(0)
n1  = int(input("Digite um número: "))
maior = n1
soma = n2 + n3
n2  = int(input("Digite um número: "))
n3  = int(input("Digite um número: "))
if(n2 > maior):
	maior = n2
	soma  = n3 + n1
	
if(n3 > maior):
	maior = n3
	soma  = n1 + n2
		
if(soma > maior):
	print("É um triangulo.")
		
else:
	print("Não é um triangulo.")