nome = [""]*4
idade = [0]*4
pessoa = []
contab = 0
media = 0
soma = 0
for cont in range(0,4,1):
    nome[cont] = str(input("Digite o nome: "))
    idade[cont] = int(input("Digite a idade: "))
    soma = soma + idade[cont]
media = soma / 4
for cont in range(0,4,1):
    if(idade[cont] > media):
        pessoa.append(nome[cont])
    elif(idade[cont] < media):
        contab = contab + 1
print(f"A média foi: {media}")
print(f"Pessoas com idade acima da média: {pessoa}")
print(f"Pessoas com idade abaixo da média: {contab}")