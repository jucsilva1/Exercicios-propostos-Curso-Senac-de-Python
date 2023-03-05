venda = float(0.00)
ano   = int(0)

venda = float(input("Quanto você vendeu este mês? "))
comissao = float(0.00)
if(venda >= 22000):
    ano = int(input("Está a quanto tempo nesta empresa? "))
    if(ano == 2):
        comissao = venda * 0.03
    if(ano >= 3):
        comissao = venda * 0.04  
    if(ano < 2):
        comissao = venda * 0.02
    print("A comissão do vendedor é {} .".format(comissao))    
else:
    print("Você receberá somente salário fixo e não tem comissão.")
