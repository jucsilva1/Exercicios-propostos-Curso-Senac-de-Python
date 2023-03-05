nota = [0]*7
cont = 0
media = float(0.00)
soma = 0
maior = 0
menor = 9999

for cont in range(0,6,1):
    nota[cont] = float(input("Digite sua nota: "))
    soma = soma + nota[cont]
media = soma / 6
for cont in range(0,6,1):
    if(nota[cont] > media):
        print(f"Acima da média: {nota[cont]}.")
    if(nota[cont] > maior):
        maior = nota[cont]
    if(nota[cont] < menor):
        menor = nota[cont]
print(f"A média das notas: {media}.")
print(f"A maior das notas: {maior}.")
print(f"A menor das notas: {menor}.")