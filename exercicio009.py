divida = int(input("Quanto você deve? "))
tempo = int(input("Qual o tempo dessa dívida em meses? "))
taxa = int(input("Qual a taxa de juros aplicada ao mês? "))
juros = float(divida * tempo * taxa/100)
total = float(divida + juros)
print("A sua dívida que era de {} a {} meses a uma taxa de {}(%) e gerou {} de juros finalizando um total de {} .".format(divida, tempo, taxa, juros, total))