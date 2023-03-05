h = int(0)
cidade = str("")
idade = int(0)
print("[1] Fabio Porchat")
print("[2] Danilo Gentilli")
print("[3] Fafinha Bastos")
h = int(input("Escolha um dos humoritas: "))
cidade = str(input("Qual é a cidade? "))
match (h):
    case 1:
        if(cidade == "Araxá"):
            idade = int(input("Qual é a sua idade? "))
            if(idade >= 18):
                print("Tem show do Fabio Porchat!")
            else:
                print("Não tem show!")
    case 2:
        if(cidade == "São Paulo"):
            print("Tem show do Danilo Gentilli!")
        else:
            print("Não tem show!")
    case 3:
        if(cidade == "Porto Alegre"):
            print("Tem show de Rafinha Bastos")
        else:
            print("Não tem show!")
    case _:
        print("Escolha de humorista inválido!")