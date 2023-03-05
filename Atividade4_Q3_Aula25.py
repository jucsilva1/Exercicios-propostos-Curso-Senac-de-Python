pessoas = []

for i in range(4):
    nome = str(input(f"Insira o nome da pessoa {i + 1}: "))
    idade = int(input(f"Insira a idade da pessoa {i + 1}: "))
    pessoas.append((nome, idade))
total_idade = 0
for nome, idade in pessoas:
    total_idade += idade
media_idade = total_idade / len(pessoas)

abaixo_media_nomes = [nome for nome, idade in pessoas if idade > media_idade]
abaixo_media = 0
for nome, idade in pessoas:
    if idade < media_idade:
        abaixo_media += 1
print("A média de idade das pessoas:", media_idade)
print("Pessoas acima da média de idade:", abaixo_media_nomes)
print("Quantidade de pessoas abaixo da média de idade:", abaixo_media)
