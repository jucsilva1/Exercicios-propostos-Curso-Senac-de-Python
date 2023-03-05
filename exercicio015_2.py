import random 

a = random.randint(10,30)
b = random.randint(10,30)

multiplicacao = float(a * b)
media = float(a + b ) / 2

print("Foram sorteados os valores {} , {}, a multiplicação desses valores é {} e a média é {}.".format(a, b, multiplicacao, media))