idade = int(input("Qual sua idade? "))
nacionalidade = str(input("Qual sua nacionalidade? "))
sexo = str(input("Qual é o seu sexo? "))
situacao = idade == 18 and nacionalidade == "brasileiro" and sexo == "masculino"
print("{} anos, {} e do sexo {} sendo os dados informados geraram a situação: {}".format(idade, nacionalidade, sexo, situacao))
if(situacao == True):
    print("Apto.")
else:
    print("Não apto.")