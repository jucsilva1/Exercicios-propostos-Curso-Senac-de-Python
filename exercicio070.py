usuario = str("")
senha = str("")
multa = 2.00
rmulta = str("")
while(True):
    usuario = str(input("Digite um usuário: "))
    senha = str(input("Digite uma senha: "))
    if(usuario == "fácil" and senha == "ff"):
        print("Acesso correto!")
        break
    else:
        rmulta = str(input("Você será multado em R$2.00 pela sua falha, gostaria de tentar novamente?Sua multa está em :{}.".format(multa)))
        if(rmulta == "sim"):
            multa = multa * 2
        else:
            print("Você está indo embora mas, sua multa foi {}.".format(multa))
            break