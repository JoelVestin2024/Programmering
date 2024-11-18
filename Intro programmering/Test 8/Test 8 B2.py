import random

treor = 0
lista = []

for i in range(33):
    lista.append(random.randint(1, 3))

print("Antal treor:", lista.count(3))