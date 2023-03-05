salario  = float(input("Qual é o seu salário? "))
ferias   = salario * 1.33
bonus    = salario * 1.75
decimo13 = salario
total = float(salario + ferias + bonus +  decimo13)
print("Somando tudo seu você tem direito a R${} reais.".format(total))