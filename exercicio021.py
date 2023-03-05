import random 

sorteio = float(random.randint(1,100))
print("Se o número sorteado for no intervalo entre 18 a 35 dará resultado verdadeiro.")
print(sorteio)
res = sorteio <= 35 and sorteio >=18
print("O resultado foi: {}.".format(res))
if(res == True):
    print("Deu certo!")
else:
    print("Deu errado!")
