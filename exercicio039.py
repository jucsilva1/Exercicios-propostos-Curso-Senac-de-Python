time  = str("")
pref  = str("")  
unifc = str("")
time = str(input("Qual time você torce? "))
if(time == "atletico"):
    pref = str(input("Qual uniforme você prefere? Escolha A - para Modelo 1 ou B - para Modelo 2: "))
    if(pref == "A"):
        print("O Valor será de R$85.00")
    elif(pref == "B"):
        print("O Valor será de R$75.00")
if(time == "cruzeiro"):
    unifc = str(input("Qual uniforme você prefere? Escolha A - para Modelo 1 ou B - para Modelo 2: "))
    if(unifc == "A"):
        print("O Valor será de R$45.00")
    elif(unifc == "B"):
        print("O Valor será de R$95.00")