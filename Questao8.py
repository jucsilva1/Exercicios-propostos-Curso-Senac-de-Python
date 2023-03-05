dist = int(input("Qual a distância em quilometros? "))
hecto = dist * 10
deca  = dist * 100
metro = dist * 1000
cent  = dist * 100000
mili  = dist * 1000000

print("{} quilômetro(s) convertido(s):".format(dist))
print("Em hectômentros é {} hm, em decâmetros é {} dam, em metros é {} metros, em centímetros é {} cm, em milímetros é  {} mm.".format(hecto, deca, metro, cent, mili))