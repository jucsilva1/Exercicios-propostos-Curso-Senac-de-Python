cont = 0
nome = ""
idade = 0
sexo = ""
homem = ""
mulher = ""
midade = 0
meidade = 99999
idade = midade
idade = meidade
while(cont < 3):
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Qual é o seu sexo: M ou F: "))
    if(idade > midade and sexo == "M"):
        midade = idade
        homem  = nome
    if(idade < meidade and sexo == "F"):
        meidade = idade
        mulher  = nome
    cont = cont + 1
print("O nome do homem mais velho é {} e o nome da mulher mais jovem é {}.".format(homem, mulher))