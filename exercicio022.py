idade = str(input("Você tem mais de 25 anos de idade? sim ou nâo? "))
fala = str(input("Você fala Inglês? sim ou nâo? "))
falar = fala == "sim"
falaringles = fala == "sim" and idade == "sim"
print(falar)