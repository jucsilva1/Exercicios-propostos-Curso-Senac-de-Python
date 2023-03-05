peso = float(input("Qual é a seu peso em kilos? "))
quant = float(input("Quantos sanduiches comeu este mês? "))
medio = float(8.50)
engorda = quant * 0.10
gasto = quant * medio
total= peso + engorda
print("Sabendo que cada sanduiche você engorda 100 gramas...")
print("Seu peso após comer {} sanduiches é de {} KG e você gastou {} reais.".format(quant, total, gasto))