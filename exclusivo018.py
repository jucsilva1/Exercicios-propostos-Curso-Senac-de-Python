import random
conta = int(input("Digite o seu saldo em conta? "))
aposta = int(input("Qual valor quer apostar? "))

if(aposta > conta):
        print("Saldo insuficiente!!")
else:
    print("Pode apostar!")
    conta = conta - aposta
    opcao = float(input("Escolha seu fator de multiplicação: 1.1 : 1.3 : 1.6 : 2.0 : 2.5 sua opção: "))
    
    if(opcao == 1.1 ):
        vetor9 = ["acertou", "acertou","acertou","acertou","acertou","acertou","acertou","acertou","acertou","errou"]
        sorte9 = random.choice(vetor9)
        if(sorte9 == "acertou"):
            print("Você multiplicou sua aposta em 1.1.")
            aposta = aposta + (aposta * 1.1)
        else:
            print("errou")
            aposta = 0     
            
    elif(opcao == 1.3 ):
        vetor8 = ["acertou", "acertou","acertou","acertou","acertou","acertou","acertou","acertou","acertou","errou"]
        sorte8 = random.choice(vetor8)
        if(sorte8 == "acertou"):
            print("Você multiplicou sua aposta em 1.3.")
            aposta = aposta + (aposta * 1.3)
        else:
            print("Errou")
            aposta = 0
                
    elif(opcao == 1.6 ):
        vetor5 = ["acertou", "acertou","acertou","acertou","acertou","errou","errou","errou","errou","errou"]
        sorte5 = random.choice(vetor5)
        if(sorte5 == "acertou"):
            print("Você multiplicou sua aposta em 1.6.")
            aposta = aposta + (aposta * 2.0)
        else:
            print("Errou")
            aposta = 0
                
    elif(opcao == 2.0 ):
        vetor4 = ["acertou", "acertou","acertou","acertou","errou","errou","errou","errou","errou","errou"]
        sorte4 = random.choice(vetor4) 
        if(sorte4 == "acertou"):
            print("Você multiplicou sua aposta em 2.0.")
            aposta = aposta + (aposta * 2.0)
        else:
            print("Errou")
            aposta = 0  
               
    elif(opcao == 2.5):
        vetor2 = ["acertou", "acertou","errou","errou","errou","errou","errou","errou","errou","errou"]
        sorte2 = random.choice(vetor2)
        if(sorte2 == "acertou"):
            print("Você multiplicou sua aposta em 2.5.")
            aposta = aposta + (aposta * 2.5)
        else:
            print("Errou")
            aposta = 0
    else: 
        print("Você perdeu!")
        aposta = 0    
    conta = conta + aposta
print (f"Seu saldo atual é {conta}")