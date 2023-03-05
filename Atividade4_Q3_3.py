galera = list()
pessoa = dict()
soma = 0
media = float(0.00)
while(True):
    pessoa.clear()
    pessoa["nome"] = str(input("nome: "))
    pessoa["idade"] = int(input("Idade: "))
    soma = soma + pessoa["idade"]
    galera.append(pessoa.copy())
    while(True):
        resp = str(input("Quer continuar? [S/N] "))
        if(resp in "SN"):
            break
        print("Erro! Responda apenas S ou N. ")
    if(resp == "N"):
        break
print("-=" * 30)
print(f"Ao todo temos {len(galera)} pessoas cadastradas.")
media = soma / len(galera)
print(f"A média de idade é de {media} anos.")
print(f"As mulheres cadastradas foram ", end=" , ")
for pessoa in (galera):
    if pessoa["sexo"] in "Ff":
        print(f'{pessoa["nome"]} ', end=" , ")
print()
print(f"Lista de pessoas que estão acima da média")
for pessoa in (galera):
    if pessoa["idade"] > media:
        print(" ", end=" - ")
        for k, v in pessoa.items():
            print(f'{k} = {v} ', end="")
        print()
print("<< ENCERRADO >>")