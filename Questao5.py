salario = float(input("Qual é o seu salário? "))
ferias   = salario * 1.33
bonus    = salario * 0.74
promocao = salario * 1.45
total = float(salario + ferias + bonus)
print("Baseado no seu salário suas férias seriam R${} , seu bônus seria R${} e caso você fosse promovida seria R${}.".format(ferias, bonus, promocao))
