nome  = str("")
valor = float(0.00)
prodA = 0
prodB = 0
prodC = 0
cont  = 0
total = 0
fechar =str("")

while(True):
    nome = str(input("Nome do Produto: "))
    valor = int(input("Valor do Produto: "))
    if(valor >= 1000):
        total = total + valor
        prodA = prodA + 1
    elif(valor >= 500 and prodB <= 999.99):
        total = total + valor
        prodB = prodB + 1
    elif(valor > 0 and prodC < 499.99):
        total = total + valor
        prodC = prodC + 1
    fechar = str(input("Deseja fechar o caixa? s ou n ? "))
    if(fechar == "s"):
        break
print(f"Total da compra foi de {total}")
print(f"Foram {prodA} de padrão A.")
print(f"Foram {prodB} de padrão B.")
print(f"Foram {prodC} de padrão C.")
        