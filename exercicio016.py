valor  = float(input("Quanto você tem na sua conta? "))
compra = float(input("Qual valor das compras do mês? "))
saldo = valor - compra
if (valor < compra):
    print("O valor é insuficiente para pagar as compras.")
elif(valor >= compra):
    print("O valor é suficiente para pagar as compras e saldo de {}.".format(saldo))