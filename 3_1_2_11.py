slowo_uzytkownika = input("Wprowadz slowo: ")
slowo_uzytkownika = slowo_uzytkownika.upper()
litera = "A"
slowo_bez_samoglosek = ""

for litera in slowo_uzytkownika:
    # print(type(litera))
    if litera == "A":
        continue
    elif litera == "E":
        continue
    elif litera == "I":
        continue
    elif litera == "O":
        continue
    elif litera == "U":
        continue
    else:
        slowo_bez_samoglosek = slowo_bez_samoglosek + litera

print(slowo_bez_samoglosek)