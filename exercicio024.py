n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
resp = int(input("Escolha 1- Soma ou 2- Média : Sua opção: "))

if(resp == 1):
    somar = float(n1 + n2)
    print("A soma de {} e {} é igual a {}.".format(n1, n2, somar))
elif(resp == 2):
    media = float(n1 + n2) / 2
    print("A média de {} e {} é igual a {}.".format(n1, n2, media))
else:
    print("Escolha inválida!")