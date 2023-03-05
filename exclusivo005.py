import random

num = random.randint(0,2)
print(num)

print("Jogo do Pedra, Papel ou tesoura.")
print("[0] Pedra.")
print("[1] Papel.")
print("[2] tesoura.")
esc = int(input("Digite sua escolha: "))

if num == 0:
    print("O computador escolheu: Pedra")
    if esc == 0:
        print("Empate!")
    elif esc == 1:
        print("Jogador perdeu")
    elif esc == 2:
        print("Computador venceu")
    else:
        print("Operacao invalida")

elif num == 1:
    print("O computador escolheu: Papel")
    if esc == 0:
        print("Computador perdeu")
    elif esc == 1:
        print("Empate!")
    elif esc == 2:
        print("Jogador venceu")
    else:
        print("Operacao invalida")
elif num == 2:
    print("O computador escolheu: Tesoura")
    if esc == 0:
        print("Jogador venceu")
    elif esc == 1:
        print("Computador venceu")
    elif esc == 2:
        print("Empate!")
    else:
        print("Operacao invalida")
else:
    print("Operacao invalida")