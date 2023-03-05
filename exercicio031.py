menor = float(0.00)
s1 = float(input("Qual o salário da pessoa1? "))
menor = s1
s2 = float(input("Qual o salário da pessoa2? "))
if(s2 < menor):
    menor = s2
s3 = float(input("Qual o salário da pessoa3? "))
if(s3 < menor):
    menor = s3
s4 = float(input("Qual o salário da pessoa4? "))
if(s4 < menor):
    menor = s4

print("O menor salário entre as pessoas citadas é R$ {}".format(menor))
