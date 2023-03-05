num = 0
resp = str("")
cont = 0
gr025 = 0
gr2650 = 0
gr5175 = 0
gr76100 = 0

while(True):
    num = int(input("Digite um número: "))
    resp = str(input("Deseja continuar? s ou n : "))
    if(num >= 0 and num <= 25):
        gr025 = gr025 + 1
    if(num >= 26 and num <= 50):
        gr2650 = gr2650 + 1
    if(num >= 51 and num <= 75):
        gr5175 = gr5175 + 1
    if(num >= 76 and num <= 100):
        gr76100 = gr76100 + 1
    if( resp == "n"):
        break
    if( num < 0 and num > 100):
        break
print("A quantidade de números do grupo 0-25 é: {}.".format(gr025))
print("A quantidade de números do grupo 26-50 é: {}.".format(gr2650))
print("A quantidade de números do grupo 51-75 é: {}.".format(gr5175))
print("A quantidade de números do grupo 76-100 é: {}.".format(gr76100))
