lista = [2, 3, 2, 4, 1]
lista[1] = 5
lista[4] = 6
lista.append(4)
print("Medelvärdet:", sum(lista)/len(lista))
lista.sort()
print(lista)