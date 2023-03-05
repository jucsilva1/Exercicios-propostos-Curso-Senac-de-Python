datas = str("")
comemora = str("")
ter = str("")

datas = str(input("Que dia é hoje? formato 99/99/9999 : "))
if(datas == "19/01/2023"):
    comemora = str(input("Você sabe o que se comemora nesse dia? "))
if(comemora == "melhor quinta-feira da semana"):
	ter = str(input("Você sabe o que vai ter no Senac hoje? "))
if(ter == "sim"):
        print("Então você já sabe da surpresa inesperada, nesse caso a surpresa nem é tão inesperada assim.")
else:
    print("Hoje é o dia de uma surpresa inesperada!")   