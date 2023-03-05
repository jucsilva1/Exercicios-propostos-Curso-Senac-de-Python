num = 0
cont = 0
resp = str("")
sneg = 0
cpos = 0
spos = 0
cneg = 0
mediapos = 0
while (True):
    num = int(input("Digite um número: "))
    resp = str(input("Deseja continuar? s ou n : "))
    if(num > 0):
        cpos = cpos + 1
        spos = spos + num
    if(num < 0 ):
        cneg = cneg + 1
        sneg = sneg + num
    if(resp == "n"):
        mediapos = spos/cpos
        print("A média aritmética dos positivos é {}.".format(mediapos))
        break
    cont = cont + 1
print("A quantidade de negativos foi de {} e sua soma é {} e quantidade de positivos foi de {} e sua soma é {}.".format(cneg, sneg, cpos, spos))
    
    
    
    