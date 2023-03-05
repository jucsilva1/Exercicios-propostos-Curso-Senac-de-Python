sexo = str("")

while(True):
    sexo = str(input("Digite o sexo: "))
    if(sexo == "m" or sexo == "f"):
        print(f"O sexo digitado foi {sexo} cadastrado com sucesso!")
        break
    else:
        print("Sexo inexistente! Tente novamente!")
