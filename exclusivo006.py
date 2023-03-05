import random

num = random.randint(0,4)
print(num)

print("Jogo do Pedra, Papel, Tesoura, Lagarto ou Spock.")
print("[0] Pedra.")
print("[1] Papel.")
print("[2] Tesoura.")
print("[3] Lagarto.")
print("[4] Spock.")
esc = int(input("Digite sua escolha: "))

if (num == 0):
    print("O computador escolheu: Pedra")
    if esc == 0:
        print("Empate!")
    elif (esc == 1):
        print("Jogador ganhou")
    elif (esc == 2):
        print("Computador venceu")
    elif (esc == 3):
        print("Computador venceu")
    elif (esc == 4):
        print("Jogador ganhou")
    else:
        print("Operacao invalida")

elif (num == 1):
    print("O computador escolheu: Papel")
    if (esc == 0):
        print("Computador venceu")
    elif (esc == 1):
        print("Empate!")
    elif (esc == 2):
        print("Jogador venceu")
    elif (esc == 3):
        print("Jogador venceu")
    elif (esc == 4):
        print("Computador ganhou")
    else:
        print("Operacao invalida")
        
elif (num == 2):
    print("O computador escolheu: Tesoura")
    if (esc == 0):
        print("Jogador venceu")
    elif (esc == 1):
        print("Computador venceu")
    elif (esc == 2):
        print("Empate!")
    elif (esc == 3):
        print("Computador venceu")
    elif (esc == 4):
        print("jogador ganhou")
    else:
        print("Operacao invalida")

elif (num == 3):
    print("O computador escolheu: Lagarto")
    if (esc == 0):
        print("Jogador venceu")
    elif (esc == 1):
        print("Computador venceu")
    elif (esc == 2):
        print("jogador venceu")
    elif (esc == 3):
        print("Empate!")
    elif (esc == 4):
        print("Computador venceu")    
    else:
        print("Operacao invalida")
        
elif (num == 4):
    print("O computador escolheu: Spock")
    if (esc == 0):
        print("Computador venceu")
    elif (esc == 1):
        print("Jogador venceu")
    elif (esc == 2):
        print("Computador venceu")
    elif (esc == 3):
        print("Jogador venceu")
    elif (esc == 4):
        print("Empate!")  
    else:
        print("Operacao invalida")
else:
    print("Operacao invalida")

    
    