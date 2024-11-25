
text_input = input("Skriv ett ord som inehåller bokstaven A:")
text_output = []

for i in text_input:
    if i == "a":
        text_output.append("ä")
    else:
        text_output.append(i)

for i in text_output:
    print(i)

