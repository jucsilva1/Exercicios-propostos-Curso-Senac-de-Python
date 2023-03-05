idade = 0
sexo = str("")
cpe = 0
cho = 0
cmu = 0
parar = str("")
while(True):
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo: m ou f ? "))
    parar = str(input("Deseja continuar? s ou n ? "))
    if(idade > 10):
        cpe = cpe + 1
    if(sexo == "m"):
        cho = cho + 1
    if(sexo == "f" and idade < 20):
        cmu = cmu + 1
    if(parar == "n"):
        break
print(f"Pessoas com mais de 10 anos foi :{cpe}.")
print(f"Foram cadastrados {cho} homens.")
print(f"Foram cadastradas {cmu} mulheres com menos de 20 anos.")