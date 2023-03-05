nome = str("")
idade = 0
cont = 0
cont2 = 0
while(nome != "João"):
    nome = str(input("Digite seu nome: "))
    cont = cont + 1
while(True):
    idade = int(input("Digite sua idade: "))
    if(idade >= 35 and nome == "João"):
        break
    else:
        cont2 = cont2 + 1
print(f"Você tentou {cont} vez(es) antes de acertar o nome e {cont2} vez(es) a idade.")
