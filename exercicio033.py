maior = float(0.0)
nome = str("")
p1 = str(input("Qual o nome da pessoa1? "))
s1 = float(input("Qual é o seu salário? "))
maior = s1
nome = p1
p2 = str(input("Qual o nome da pessoa2? "))
s2 = float(input("Qual é o seu salário? "))
if(s2 > maior):
    maior = s2
    nome =  p2
p3 = str(input("Qual o nome da pessoa3? "))
s3 = float(input("Qual é o seu salário? "))
if(s3 > maior):
    maior = s3
    nome = p3
p4 = str(input("Qual o nome da pessoa4? "))
s4 = float(input("Qual é o seu salário? "))
if(s4 > maior):
    maior = s4
    nome = p4

print("O maior salário é do funcionário de nome {} com o valor de R${}".format(nome, maior))