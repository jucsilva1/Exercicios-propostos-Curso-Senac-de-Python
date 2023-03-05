veloc = int(input("Qual a velocidade? "))
if(veloc <= 80):
    print("Velocidade segura!")
elif(veloc > 80):
    excesso = int(veloc - 80)
    multa = int(450 +(excesso * 10))
    print("Limite de velocidade excedido. Sua multa é {}.".format(multa))