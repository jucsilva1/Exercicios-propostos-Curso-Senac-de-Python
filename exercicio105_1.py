while(True):
    jogar = str(input("Quer jogar? "))
    if(jogar == "sim"):
        aposta = float(input("Quanto você quer apostar? "))
        import random
        if(vitoria < 5):
            vetor    = ["cristal","bomba","cristal","bomba","cristal","cristal","cristal"]
        elif(vitoria > 5 and vitoria < 10):
            vetor = ["cristal","bomba","cristal","bomba"]
            multiplicador = 1.5
        else:
            vetor = ["cristal","bomba","bomba","bomba"]
            vitoria = vitoria - 1
            multiplicador = 1.2
             
        contl = 0
        contc = 0
        sorte = ["","","",""],["","","",""],["","","",""],["","","",""]
        derrota = 0
        vitoria = 0
        multiplicador = 2
        for contl in range(0,4,1):
            for contc in range(0,4,1):
                sorte[contl][contc] = random.choice(vetor)
                    
        print(sorte[0])   
        print(sorte[1]) 
        print(sorte[2])     
        print(sorte[3]) 

        while(True):
            linha = int(input("Escolha o primeiro número para o jogo Campo Minado: "))
            coluna = int(input("Escolha o segundo número para o jogo Campo Minado: "))
            if(sorte[linha][coluna] == "bomba"):
                print("Você perdeu!")
                derrota = derrota + 1
                aposta = 0
                break
            else:
                print("Você ganhou!")
                vitoria = vitoria + 1
                aposta = aposta * multiplicador
                parar = str(input("Deseja parar? "))
                if(parar == "sim"):
                    break
        print(f"Seu resultado final foi {aposta} vez(es).")
    else:
        break