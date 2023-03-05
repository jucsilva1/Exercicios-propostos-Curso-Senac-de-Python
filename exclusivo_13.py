num = 0
cont = 0
soma = 0
resto = 0
while(cont < 200):
    num = int(input("Digite um valor: "))
    soma = soma + num
    if(soma >= 1000):
        resto = soma - 1000
        print(f"Excedeu em {resto}.")
        break