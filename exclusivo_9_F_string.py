cont = 0
cmarcos = 0
while(cont < 5):
    nome = str(input("Digite um nome: "))
    if( nome == "Marcos"):
        cmarcos = cmarcos + 1
    cont = cont + 1
print(f"Foram cadastrado(s) {cmarcos} Marcos de um total de {cont} nomes.")
    