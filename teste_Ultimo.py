nome = [""]*4
cont = 0
idade = [0]*4
amedia = 0
abmedia = 9999
soma = 0
media = 0
conta = 0
for cont in range(0,4,1):
    idade = int(input("Digite sua idade: "))
    nome = str(input("Digite seu nome: "))
    soma = soma + idade
for n in nome:
    if(idade > media):
        amedia = idade
        namedia = nome
    print(n)
    if(idade < media):
        conta = conta + 1
media = soma / 4    
print(f"A média de idade das pessoas cadastradas é: {media}.")
print(f"O(s) nome(s) da(s) pessoa(s) que estão acima da média de idade cadastradas é: {namedia}.")
print(f"Pessoas cadastradas abaixo da média das idades é: {conta}")