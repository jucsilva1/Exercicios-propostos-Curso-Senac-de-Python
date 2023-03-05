veloc = int(input("Qual a velocidade? "))
if(veloc <= 80):
    print("Velocidade segura!")
elif(veloc > 80 and veloc <= 100):
    excesso = int(veloc - 80)
    multa = int(150 +(excesso * 5))
    print("Limite de velocidade excedido. Sua multa é {}.".format(multa))
elif(veloc > 100 and veloc <= 160):
    excesso = int(veloc - 80)
    multa = int(250 +(excesso * 10))
    print("Limite de velocidade excedido. Sua multa é {}.".format(multa))
elif(veloc > 160 and veloc <= 280):
    excesso = int(veloc - 80)
    multa = int(500 +(excesso * 20))
    print("Limite de velocidade excedido. Sua multa é {}.".format(multa))    
else:
    print("O veículo será confiscado!")