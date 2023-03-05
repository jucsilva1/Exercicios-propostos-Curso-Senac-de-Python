saldo = float(0.0)
valor  = float(input("Quanto você tem na sua conta? "))
compra1 = float(input("Qual valor da sua primeira compra? "))
compra2 = float(input("Qual valor da sua segunda compra? "))
total = compra1 + compra2

if (valor < total):
    print("Você não tem dinheiro suficiente é hora de devolver as compras.")
elif(valor > total):
    saldo = valor - total
    print("Você ainda tem {} reais então pode gastar mais.".format(saldo))
else:
    saldo = valor - total
    print("Você conseguiu pagar as compras porém ficou sem saldo R${}.".format(saldo))
    
