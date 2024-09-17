
n = 42
gissa = int(input("Gissa på ett tal mellan 1 och 100: "))
while n!= gissa:
    if gissa < n:
        print("För litet")
        gissa = int(input("Försök igen: "))
    elif gissa > n:
        print("För stort")
        gissa = int(input("Försök igen: "))
    else:
      break
print("Du gissade rätt!!")