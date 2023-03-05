dist = int(0.00)

dist = int(input("Qual a distância(Km) da corrida do Uber? "))
taxa = float(0.00)

if(dist <= 200):
	taxa = dist * 0.35
else:
	taxa = dist * 0.20
 
perigoso = str("")
total = float(0.00)
perigoso = str(input("O bairro de destino é perigoso? "))

if(perigoso == "sim"and dist <= 200 ):
	total = total + (taxa * 2)
 
if(perigoso == "sim" and dist > 200):
	    total = total + (taxa * 1.8)
else:
    total = taxa     
    
    
print("O valor final da corrida para o destino é {}.".format(total))