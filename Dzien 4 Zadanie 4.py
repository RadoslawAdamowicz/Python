lista1 = []
lista2 = []
wynik = False

dlugosc1 = int(input("Podaj długość pierwszej listy "))
print()
print("Lista pierwsza")

for i in range(dlugosc1):
    element = input("Podaj element listy = ")
    lista1.append(element)

print()
dlugosc2 = int(input("Podaj długość drugiej listy "))
print()
print("Lista druga")

for i in range(dlugosc2):
    element = input("Podaj element listy = ")
    lista2.append(element)

for i in range(dlugosc1):
    for ii in range(dlugosc2):
        if lista1[i] == lista2[ii]:
            wynik = True

print()
if wynik == True: print("Listy maja wspólny element")
else: print("Listy nie maja wspólnego elementu")