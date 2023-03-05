p = int(0)
r1 = int(input("Quanto é 2 + 2? "))
if(r1 == 4):
    p = p + 1
r2 = str(input("O que é um trem? "))
if(r2 == "veiculo"):
    p = p + 1
r3 = str(input("Qual é a melhor segunda-feira da semana? "))
if(r3 == "hoje"):
    p = p + 1
print("Você obteve {} pontos.".format(p))