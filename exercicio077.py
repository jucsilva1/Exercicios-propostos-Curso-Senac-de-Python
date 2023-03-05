limite = float(0.00)
valorc = float(0.00)
limite = float(input("Qual é o limite de crédito? "))

while(True):
    valorc = float(input("Qual valor de sua compra? "))
    if(limite >= valorc):
        print("Compra realizada com sucesso!")
        limite = limite - valorc
        print(f"Você ainda tem um saldo de R${limite}")
    else:
        print("Saldo insuficiente!!")
        break