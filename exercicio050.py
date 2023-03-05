n1 = float(0.00)
n2 = float(0.00)
op = str("")
soma = float(0.00)
subtracao = float(0.00)
multiplicacao = float(0.00)
divisao = float(0.00)	
	
n1 = float(input("Digite um número: "))
		
n2 = float(input("Digite outro número: "))

print("\nEscolha que opareção deseja fazer:")
print("\n---------------------------------- \n")
print("1 - Soma \n")
print("2 - Subtração \n")
print("3 - Multiplicação \n")
print("4 - Divisão \n")
op = int(input("Opção: "))		

soma = n1 + n2	
subtracao = n1 - n2   
multiplicacao = n1 * n2   
divisao = n1 / n2
match op:

        case 1:
            print("A soma de {} + {} é = {}.".format(n1, n2, soma))

        case 2:
        

            print("A subtração de {} - {} é = {}.".format(n1, n2, subtracao))

        case 3:

            print("A multiplicação de {} * {} é = {}.".format(n1, n2, multiplicacao))

        case 4:

            print("A divisão de {} / {} é = {}.".format(n1, n2, divisao))

        case _:

            print("Você não escolheu uma opção válida!")

  