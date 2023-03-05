reais = float(input("Quantos reais tem na sua conta bancária? "))
dolar = float(reais/5.23)
euro  = float(reais/5.52)
iene  = float(reais/0.038)

print("Você tem o equivalente {} dolares.".format(dolar))
print("Você tem o equivalente {} euros.".format(euro))
print("Você tem o equivalente a {} ienes.".format(iene))
