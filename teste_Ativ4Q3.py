vetor = [["","","",""]]
vetori = [[0,0,0,0]]
cont = 0
conti = 0
media = float(0.00)
somai = 0
cmedia = 0
nmedia = str("")
for cont in range(0,4,1):
    for conti in range(0,4,1):
        vetor[cont][conti] = str(input("Digite seu nome: "))
        vetori[cont][conti] = int(input("Digite sua idade: "))
        somai = somai + vetori
        if(vetori > media):
            nmedia = vetor[cont][conti]
        if(vetori < media):
            cmedia = cmedia + 1
media = somai / 4