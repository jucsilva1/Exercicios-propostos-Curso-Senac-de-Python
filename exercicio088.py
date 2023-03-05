cont = 0 
nome = str("")
sexo = str("")
m = 0 
for cont in range(0, 3, 1):
    nome = str(input("Digite um nome: "))
    sexo = str(input("Digite o sexo: m ou f : "))
    if(sexo == "m"):
        m = m + 1
print(f"A quantidade de homens cadastrados foi: {m}")
    