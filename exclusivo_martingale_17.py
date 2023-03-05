cor = ["vermelho","branco","preto"]
tentativa = 0
roubo = 0
import random
while(True):
    roubo = roubo + 1
    if(roubo == 100):
        sorteio = random.choice(cor)
        cor = "vermelho"
        if(sorteio == "preto"):
            tentativa = tentativa + 1
            break
        else:
            tentativa = tentativa + 1
print(f"O número de tentativas para ganhar a 2 reais {tentativa}")