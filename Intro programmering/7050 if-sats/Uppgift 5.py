tal1 = int(input("Skriv första talet: "))
tal2 = int(input("Skriva andra talet: "))
tal3 = int(input("Skriv tredje talet: "))

if (tal1 >= tal2) and (tal1 >= tal3):
    störst = tal1
elif (tal2 >= tal1) and (tal2 >= tal3):
    störst = tal2
else:
    störst = tal3

print("Det största talet av", tal1, ",", tal2, "och", tal3, "är", störst)