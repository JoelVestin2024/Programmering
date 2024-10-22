import random

def kasta_tarningar():
    # Slumpar två värden mellan 1 och 6 för tärningarna
    tarning1 = random.randint(1, 6)
    tarning2 = random.randint(1, 6)
    return tarning1, tarning2

def spela():
    while True:
        # Frågar spelaren om de vill spela
        spela_igen = input("Vill du spela? j/n: ").lower()
        if spela_igen == 'n':
            print("Vad roligt att du spelade en stund!")
            break
        elif spela_igen == 'j':
            tarning1, tarning2 = kasta_tarningar()
            print(f"{tarning1} {tarning2}")
            
            # Kontrollera om det är vinst eller förlust
            if tarning1 == 6 and tarning2 == 6:
                print("sex-vinst!")
            elif tarning1 == tarning2:
                print("vinst")
            elif tarning1 == tarning2 + 1:
                print("steg-vinst")
            elif tarning1 == tarning2 - 1:
                print("steg-vinst")
            else:
                print("förlust")
        else:
            print("Ogiltigt val, välj 'j' för ja eller 'n' för nej.")

# Starta spelet
spela()