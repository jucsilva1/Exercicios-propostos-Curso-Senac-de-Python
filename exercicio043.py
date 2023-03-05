p1  = int(0)
p2  = int(0)

cat1 = str("")
cat2 = str("")

p1 = int(input("Digite a idade da pessoa 1: "))
if(p1 <= 9):
    cat1 = "Mirim"
    
if(p1 >= 10 and  p1 <= 14):
    cat1 = "Infantil"
   
if(p1 >= 15 and  p1 <= 18):
    cat1 = "Jovem"
   
if(p1 >= 19 and  p1 <= 24 ):
    cat1 = "Adulto"
 
print("A idade da pessoa 1 é {} e a categoria é {}. ".format(p1, cat1))

p2 = int(input("Digite a idade da pessoa 2: "))
if(p2 <= 9):
    cat1 = "Mirim"
    cat2 = "Mirim"
if(p2 >= 10 and  p2 <= 14):
    
    cat2 = "Infantil"
if(p2 >= 15 and  p2 <= 18):
    
    cat2 = "Jovem"
if(p2 >= 19 and  p2 <= 24 ):
    
    cat2 = "Adulto"
print("A idade da pessoa 2 é {} e a categoria é {}. ".format(p2, cat2))

if(cat1 == cat2):
        hora = str("")
        hora = str(input("Qual o horário da luta? "))
        print("Está marcado a luta de uma pessoa com {} de idadde e outra pessoa com {} de idade para o horário das {}.".format(p1, p2, hora))
else:
        print("Não teremos luta por não serem da mesma categoria!")




