preco = float(input("Qual o preço do produto? "))
desconto = float(input("Qual desconto em (%)? "))

desc = float(desconto/100) 
total = float(preco - (preco * desc))

print("O produto custava {} mas teve desconto de {} % por isso está custando {} reais.".format(preco, desconto, total))