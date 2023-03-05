a = 6
b = 2
c = 20
d = 17
t1 = 0
t2 = 0
t3 = 0

t1 = a
a = c
c = t1

t2 = c
c = b
b = t2

t3 = d
d = b
b = t3
b = a
a = t3

# Deve retornar a=17, b=20, c=2, d=6
print(f"Variável a: {a}")
print(f"Variável b: {b}")
print(f"Variável c: {c}")
print(f"Variável d: {d}")
