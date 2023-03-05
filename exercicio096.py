a = 4
b = 11
c = 2
t1 = 0
t2 = 0

t1 = a
a = c
c = t1

t2 = c
c = b
b = t2

print(f"Variável a : {a}")
print(f"Variável b : {b}")
print(f"Variável c : {c}")