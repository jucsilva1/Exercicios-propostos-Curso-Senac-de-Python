import random 

sorteion1 = random.randint(0, 10)
sorteion2 = random.randint(0, 10)
sorteion3 = random.randint(0, 10)
sorteion4 = random.randint(0, 10)
print("Para simples conferência: os núemros sorteados",sorteion1,sorteion2,sorteion3,sorteion4)
	
n1 = int(input( "Digite o primeiro número: "))
n2 = int(input( "Digite o segundo número: "))
n3 = int(input( "Digite o terceiro número: "))
n4 = int(input( "Digite o quarto número: "))

if(n1 == sorteion1 and n2 == sorteion2 and n3 == sorteion3 and n4 == sorteion4):
		print("Você tirou o grande prêmio de R$100.000,00.")	
elif(n1 == sorteion1 and n2 == sorteion2  or n3 == sorteion3 and n4 == sorteion4):
		print("Você não ganhou, mas troque esse bilhete por outro gratuitamente.")
else:
		print("Mais sorte na próxima.")	
