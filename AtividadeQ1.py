goku = 0
cell = 0
vegeta = 0

print("Jogo dos personagens Dragon Ball Z")
print("[1] goku")
print("[2] cell")
print("[3] vegeta")

persona = str(input("Algum deste personagens tem cabelo? "))
if(persona == "sim"):
    goku = goku + 1 
else:
    cell = cell + 1
    vegeta = vegeta + 1
        
p2 = str(input("Este personagem é um adulto? "))
if(p2 == "sim"):
    cell = cell + 1
else:
    goku = goku + 1
    vegeta = vegeta + 1

p3 = str(input("Este personagem é melhor que Goku? "))
if(p3 == "sim"):
    vegeta = vegeta + 1
else:
    goku = goku + 1
    cell = cell + 1
print("O personagem Goku fez  {} pontos.".format(goku))
print("O personagem Cell fez {} pontos.".format(cell))
print("O personagem Vegeta fez  {} pontos.".format(vegeta))
