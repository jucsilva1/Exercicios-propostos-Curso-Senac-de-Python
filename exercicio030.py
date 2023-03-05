evelin = int(0)
mike = int(0)
max = int(0)
robin = int(0)
liv = int(0)
joel = int(0)
chrissy = int(0)
hopper = int(0)
joyce = int(0)
murray = int(0)

p1 = str(input("Estão todos personagens na 4 temporada? "))
if(p1 == "sim"):
        evelin = evelin + 1
        mike   = mike + 1
        max    = max + 1
        robin  = robin + 1
        hopper = hopper + 1
        joyce  = joyce + 1
        murray = murray + 1
p2 = str(input("Tem participantes especiais neste seriado? "))
if(p2 == "sim"):
        liv  = liv + 1
        joel = joel + 1
p3 = str(input("Teve gente assassinada na série? "))
if(p3 == "sim"):
        chrissy = chrissy + 1
p4 = str(input("Teve atores que voltaram para a prisão? "))
if(p4 == "sim"):
        hopper = hopper + 1
        joyce  = joyce + 1
        murray = murray + 1
print("A  Evelin tem {} pontos.".format(evelin))
print("O  Mike tem {} pontos.".format(mike))
print("O  Max tem {} pontos.".format(max))
print("A  Robin tem {} pontos.".format(robin))
print("A  Liv tem {} pontos.".format(liv))
print("O  Joel tem {} pontos.".format(joel))
print("A  Chrissy tem {} pontos.".format(chrissy))
print("O  Hopper tem {} pontos.".format(hopper))
print("A  Joyce tem {} pontos.".format(joyce))
print("O  Murray tem {} pontos.".format(murray)) 