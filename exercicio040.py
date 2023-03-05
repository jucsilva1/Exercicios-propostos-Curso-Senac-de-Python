idade = int(0)
sexo  = str("")
nac   = str("")

idade = int(input("Qual é a sua idade? "))
if(idade == 18):
    sexo = str(input("Qual é o seu sexo? "))
    if(sexo == "masculino"):
        nac = str(input("Qual é a sua nacionalidade? "))
        if(nac == "brasileiro"):
            print("Bem vindo soldado!")
        else:
            print("Dispensado!")
    else:
        print("Dispensado!")
else:
    print("Dispensado!")