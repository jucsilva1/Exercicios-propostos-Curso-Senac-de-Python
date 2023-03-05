# 1- Exemplo
#vetor = [[17,30,20],[30,40,50],[51,61,71]]
#print(vetor[0])
#print(vetor[1])
#print(vetor[2])

#print(vetor[1]) # [30,40,50]
#print(vetor[1][1]) # 40

#print(vetor[2][1]) # 61
#print(vetor[2][0]) # 51

#vetor = [["Jose","Rua","Araxá"]["Pedro","Rua B","Araxá"]["Caio","Rua C","Araxá"]]
vetor = [["A","A","A"],["Pedro","Rua B","Araxá"],["Caio","Rua C","Araxá"]]
cont = 0
grupo = 0

for grupo in range(0,3,1):
    for cont in range(0,3,1):
        vetor[grupo][cont] = str(input("Digite algo"))
    


#for cont in range(0,3,1):
 #   vetor[0][cont] = str(input("Digite algo: "))

#for cont in range(0,3,1):
 #   vetor[1][cont] = str(input("Digite algo: "))

#for cont in range(0,3,1):
 #   vetor[2][cont] = str(input("Digite algo: "))
print(vetor[0])
print(vetor[1])
print(vetor[2])

