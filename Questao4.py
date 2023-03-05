pessoas = int(input("Quantas pessoas foram mortas por este criminoso? "))
pena = int((pessoas * 3) -3)
tempo = int(pena + 15)
print("Esse criminoso pegará {} anos de cadeia.".format(tempo))

crime = str(input("Comenteu algum outro crime? sim ou nao ? "))
penaextra = int(tempo * 2)
if(crime == "sim"):
    print("Sua pena será o dobro da pena ficando um total de {} anos.".format(penaextra))
elif(crime == "nao"):
    print("Seu tempo de prisão será mantido com a pena de {} anos de prisão.".format(tempo))
else:
    print("Opção inválida!")