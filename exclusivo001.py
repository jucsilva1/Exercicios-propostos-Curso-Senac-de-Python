km = int(0)
dias = int(0)

km = int(input("Quantos quilômetros foram percorridos? "))
dias = int(input("Quantos dias de aluguel? "))

aluguel = float(60.00)
taxa = km * 0.15
total = aluguel * dias + (taxa)

print("O preço final é R$ {}.".format(total))