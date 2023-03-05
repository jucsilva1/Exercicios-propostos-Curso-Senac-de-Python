a = [0]*3
a[0] = 23
a[1] = 42
a[2] = 30
print(a)

b = "zeze"
print(b[3])

nome = [""]*3
cont = 0
for cont in range(0,3,1):
    nome[cont] = str(input("Digite um nome: "))
print(nome)
#print(F"O nome cadastrado foi {nome}.")

#print(F"O nome cadastrado foi {nome[0]}.")
#print(F"O nome cadastrado foi {nome[1]}.")
#print(F"O nome cadastrado foi {nome[2]}.")

# PARA EVITAR ESCREVER OS 3 PRINT E SE FOSSE 40 PRINTS SOLUÇÃO ABAIXO
for cont in range(0,3,1):
    print(F"O nome cadastrado foi {nome[cont]}.")

alunos = ['Ester','Sara','Sarah','Julio','Ana Julia','David','Thales','Lucas','Lavinia','Natalia','Ana Luiza']
import random
sorte = random.choice(alunos)
print(f"Quem vai pagar a coca é: {sorte}")
