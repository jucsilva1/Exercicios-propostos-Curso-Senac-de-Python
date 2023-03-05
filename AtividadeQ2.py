vip = ""
normal = ""
cliente = str(input("O produto é para um cliente vip ou normal? "))

if(cliente =="vip"):
    valor = int(input("Qual valor da compra? "))
    print("Cliente Vip tem acesso às super bebida A, super bebida B e super bebida C.")
    if(valor >= 8000):
        print("Terá acesso também a super bebida D.")
if(cliente == "normal"):
    print("Cliente normal tem acesso às bebida normal A, bebida normal B e bebida normalvip C.")