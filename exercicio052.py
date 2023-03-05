preco = float(input("Qual o preço do produto? "))

print("----------------------------")
print("[1] Carnaval")
print("[2] Férias Escolares")
print("[3] Dia das Crianças")
print("[4] Black Friday")
op = int(input("[5] Natal Escolha uma época do ano: "))

match (op):
    case 1:
        preco = preco * 1.10
        print("O preço final no carnaval é {:.2f}.".format(preco))
    case 2:
        preco = preco * 1.20
        print("O preço finalnas férias escolares é {}.".format(preco))
    case 3:
        preco = preco * 1.05
        print("O preço final no dias das crianças é {}.".format(preco))
    case 4:
        preco = preco * 0.70
        print("O preço final na Black Friday é {}.".format(preco))
    case 5:
        preco = preco * 0.95
        print("O preço final no Natal é {}.".format(preco))
    
