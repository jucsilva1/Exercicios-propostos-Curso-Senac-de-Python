galera = list()
pessoa = dict()
soma = 0
media = float(0.00)
cont = 0
contab = 0
for cont in range(0,4,1):
    pessoa.clear()
    pessoa["nome"] = str(input("nome: "))
    pessoa["idade"] = int(input("Idade: "))
    soma = soma + pessoa["idade"]
    galera.append(pessoa.copy())
print("-=" * 30)
print(f"Ao todo temos {len(galera)} pessoas cadastradas.")
media = soma / len(galera)
print(f"A média de idade é de {media} anos.")
print(f"Lista de pessoas que estão acima da média")
for pessoa in (galera):
    if pessoa['idade'] > media:
        print("", end="")
        for k, v in (pessoa.items()):
            print(f'{k} = {v} ', end="")
        print()
for pessoa in (galera):
    if pessoa['idade'] < media:
        contab = contab + 1
        print("", end="")
print(f"Quantidade de pessoas que estão abaixo da média de idade: {contab}")
print("<< ENCERRADO >>")