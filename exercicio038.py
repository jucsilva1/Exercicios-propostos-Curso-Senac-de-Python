valor   = float(0.00)
salario = float(0.00)
anos    = int(0)

valor   = float(input("Qual o valor da casa? "))
salario = float(input("Qual o valor do salário? "))
anos    = int(input("Quanto tempo pretende parcelar o valor da casa? "))

mensal = float(valor /(anos * 12))
total  = float(salario * 0.30)

if(mensal <= total):
    print("Empréstimo concedido")
    print("Com um salário de {} e com uma prestação de {} .".format(salario, mensal))
else:
    print("Empréstimo negado!/n")

    print("Com um salário de {} e com uma prestação de {} .".format(salario, mensal))