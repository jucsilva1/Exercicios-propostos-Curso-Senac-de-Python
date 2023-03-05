num = 0
cont = 0 
soma = 0
while(True):
    num = int(input("Digite um número: "))
    soma = soma + num
    if( num == 999):
        soma = soma - 999
        #cont = cont - 1
        break
    cont = cont + 1
print("A soma dos números {} e foram feitas {} tentativas.".format(soma, cont))