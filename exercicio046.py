valor = float(0.00)
total = float(0.00)

valor = float(input("Qual o valor da compra? "))
desconto = float( valor *0.05)

if(valor > 500):
    total = valor - desconto
    print("O valor final da sua compra é {}.".format(total))
else: 
	print("O valor final da sua compra é {}.".format(valor))