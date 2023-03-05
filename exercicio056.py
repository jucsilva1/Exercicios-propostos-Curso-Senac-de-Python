peso = float(0.00)
altura = float(0.00)
objetivo = str("")

peso   = float(input("Digite o peso: "))
altura = float(input("Digite a altura(m): Ex: 1.73m: "))
imc    = float(peso / (altura * altura))
print(imc)
ideal  = float(21.75 * (altura * altura))
ganhar = float(ideal - peso)
perder = float(peso  - ideal)
if(imc <= 18.5):
	print("Abaixo do peso.")
	print("Coma Sanduiches.")
	objetivo = str(input("Qual seu objetivo ganhar ou perder de peso? "))
	if(objetivo == "ganhar"):
		print("Você está magro precisa ganhar {} kilos.".format(ganhar))
	else:
		print("Você não pode perder peso.")
	
if(imc >= 18.5 and imc < 25):
	print("Você já está dentro do peso ideal nâo precisa ganhar e nem perder peso.")
if(imc >= 25 and imc < 30):
	print("Você está com sobrepeso precisa perder {} kilos.".format(perder))
elif(imc >= 30 and imc < 35):    
	print("Você está com odesidade1 precisa perder {} kilos.".format(perder))
elif(imc >= 35 and imc < 40):     
	print("Você está com odesidade2 precisa perder {} kilos.".format(perder))
elif(imc >= 40):    
	print("Você está com odesidade3 precisa perder {} kilos.".format(perder))