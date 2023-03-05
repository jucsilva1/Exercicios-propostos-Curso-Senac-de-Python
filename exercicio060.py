cont   = 0 
limite = 0
pulo   = 0

cont = int(input("Escolha um número para iniciar a contagem: "))
limite = int(input("Escolha um número para o limite da contagem: "))
pulo = int(input("Escolha de quanto em quanto deve pular a contagem: "))

while(cont < limite):
    print(cont, end=" ")
    cont = cont + pulo