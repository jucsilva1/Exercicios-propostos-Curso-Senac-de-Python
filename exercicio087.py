cont = 0 
atual = 1
proximo = 0
anterior = 0
repete = 0
for i in range(0,10,):
    anterior = atual
    atual = proximo
    proximo = atual + anterior
    print(f"{atual} ->")