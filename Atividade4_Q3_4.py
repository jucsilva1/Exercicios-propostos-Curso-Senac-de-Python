nome  = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
nome = [""]
idade = [0]*3
soma = 0
cont = 0
while (cont < 3):
    soma = soma + idade
    media = soma/len(soma)
    menores = 0
    maiores = 0
    lista_inv = idade.reverse()
    for maior in idade:
        if maior > media:
            maiores += 1
    for menor in idade:
        if menor < media:
            menores += 1
    print(len(idade))
    print(idade)
    print(lista_inv)
    print(soma)
    print("%.1f"%media)
    print(maiores)
    print(menores)
    print("")
    idade = float(input("Digite sua idade: "))
print("")
print("Programa encerrado")