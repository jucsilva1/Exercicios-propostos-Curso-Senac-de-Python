c1 = float(input("Valor da compra 1: "))
c2 = float(input("Valor da compra 2: "))
c3 = float(input("Valor da compra 3: "))

soma = float(c1 +c2 + c3)
print("A soma destas compras foi: {}".format(soma))

media = float(soma)/3
print("A média destas compras foi: {}".format(media))

dobro = float(media) * 2

res = soma > dobro
print("Resultado é : {}. O dobro da média é menor que a soma.".format(dobro, res))

