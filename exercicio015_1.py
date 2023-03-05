import random 

a = random.randint(10,30)
b = random.randint(10,30)
c = random.randint(10,30)
soma = float(a + b + c )
media = float(soma / 3)

print("Foram sorteados os valores {} , {} e {} e a soma desses valores é {} e a média é {}.".format(a, b, c, soma, media))
