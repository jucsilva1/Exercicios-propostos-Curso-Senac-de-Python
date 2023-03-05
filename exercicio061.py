cont = 1
limite = 0
print('=-' * 18)
limite = int(input("Até quanto você deseja contar?: "))
while(cont <= limite):
    #cont = cont + 1
    print("{} --".format(cont),end=" ")
    if(cont %3 == 0):
        print('PIN')
    cont = cont + 1
print(" ")
print('=-' * 18)
    