valorc = float(input("Qual é o valor da compra? "))
op = 0
 
op = int(input("Escolha a forma de pagamento: 1- A vista ou Pix 2- Cartão de Débito 3- Cartão de crédito >> sua opção: "))

if(op == 1):
    total1 = valorc * 0.90
    print("O valor total da compra é R${}.".format(total1))
elif(op == 2):
    total2 = valorc * 0.95
    print("O valor total da compra é R${}.".format(total2))

if(op == 3):
    parcela = int(input("Quantas parcelas você quer dividir? "))
    if(parcela <= 3):
        totalparc = valorc * 1.05
        totalc = totalparc / parcela
        print("Sua compra de {} parcelada em {} de {} sendo um total de R${}.".format(valorc, parcela, totalc, totalparc))
    elif(parcela > 3):
        totalparc = valorc * 1.10
        totalc = totalparc / parcela
        print("Sua compra de {} parcelada em {} de {} sendo um total de R${}.".format(valorc, parcela, totalc, totalparc))