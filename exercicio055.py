conh = int(0)
op = int(0)

print("[1] Básico")
print("[2] Intermediário")
print("[3] Avançado")
op = int(input("Qual é o seu conhecimento de Excel? "))
match (op):
    case 1:
        op2 = int(input("Escolha uma fórmula: 1- SOMA, 2- MÉDIA, 3- MAXIMO Opção: "))
        match (op2):
            case 1:
                print("A fórmula da SOMA serve para somar um intervalo da planilha.")
            case 2:
                print("A fórmula da MÉDIA serve para extrair um resultado de média de um intervalo da planilha.")
            case 3:
                print("A fórmula do MAXIMO serve para somar um intervalo da planilha.")
    case 2:
        op3 = int(input("Escolha uma fórmula: 1- SE, 2- SOMASE, 3- CONT.SE Opção: "))
        match (op3):
            case 1:
                print("A fórmula do SE permite que você faça comparações lógicas entre um valor e aquilo que você espera.")
            case 2:
                print("A fórmula da SOMASE soma apenas os valores de um intervalo, em que as células correspondentes no intervalo.")
            case 3:
                print("A fórmula do CONT.SE  serve para contar o número de células que atendem a um critério.")
    case 3:
        op4 = int(input("Escolha uma fórmula: 1- ordem.eq, 2- procV, 3- procH Opção: "))
        match (op4):
            case 1:
                print("A fórmula ordem.eq retorna a posição de um número em uma lista de números.")
            case 2:
                print("A fórmula do procV O que você deseja pesquisar, onde você deseja pesquisar, o número da coluna no intervalo que contém o valor a ser retornado, retorna uma correspondência Aproximada ou Exata.")
            case 3:
                print("A fórmula do procH  serve uando seus valores de comparação estiverem localizados em uma linha ao longo da parte superior de uma tabela de dados e você quiser observar um número específico de linhas mais abaixo.")