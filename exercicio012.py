n1 = float(input("Qual sua primeira nota? "))
n2 = float(input("Qual sua segunda nota? "))
n3 = float(input("Qual sua terceira nota? "))
total = float(n1+n2+n3)
media = float(total/3)
print("A média desse aluno é {} pontos.".format(media))

n4 = float(input("Qual sua quarta nota? "))
mediaatual = float((n4 + total)/4)
print("A sua nova média é de {} pontos.".format(mediaatual))

