menor = float(0.0)
maior = float(0.0)
id1 = float(input("Qual é a idade da pessoa1? "))
menor = id1
maior = id1
id2 = float(input("Qual é a idade da pessoa2? "))
if(id2 < menor):
    menor = id2
if(id2 > maior):
    maior = id2
id3 = float(input("Qual é a idade da pessoa3? "))
if(id3 < menor):
    menor = id3
if(id3 > maior):
    maior = id3
id4 = float(input("Qual é a idade da pessoa4? "))
if(id4 < menor):
    menor = id4
if(id4 > maior):
    maior = id4

print("O mais jovem tem {} anos e o mais velho tem {} anos." .format(menor, maior))