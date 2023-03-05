print("-- Opções de Resposta --")
print("------------------------")
print("1- Nasceu rica")
print("2- Casou-se com rico")
print("3- Trabalha com política")
situacao = int(input("Como ficou rica? "))
verifica = situacao == 1 or situacao == 2 or situacao == 3
print("Resposta: {}".format(verifica))
if(situacao == 1):
    print("Nasceu rica.")
elif(situacao == 2):
    print("Casou-se com rico.")
elif(situacao == 3):
    print("Trabalha com política.")
else:
    print("Não existente!")    