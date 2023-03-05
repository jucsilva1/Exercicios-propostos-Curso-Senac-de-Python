n1 = float(0.00)
n2 = float(0.00)
freq = float(0.00)

n1 = float(input("Qual é sua primeira nota? Entre 0 - 100: "))
n2 = float(input("Qual é sua segunda nota? Entre 0 - 100: "))
media = float(n1 + n2) / 2

freq = float(input("Qual é sua frequência? "))
if(media >= 60 and freq > 75):
    print("Aprovado!")
else:
    print("Reprovado!")

if(media >= 40 and freq <= 75):
    print("Está de recuperação!")
    rec = float(input("Qual é a nota de recuperação? "))
    if(rec <= 69.99):
        print("Reprovado!")
    else:
        print("Aprovado!")
if(media < 40):
    print("Reprovado sem direito a recuperação!")        