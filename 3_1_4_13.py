# Krok 1
beatles = []
print("Krok 1:", beatles)

# Krok 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Krok 2:", beatles)

# Krok 3
i=""
while i!="0":
    i = input("Dodaj muzyka (0 by zakończyć): ")
    if i=="0": break
    beatles.append(i)
print("Krok 3:", beatles)

# Krok 4
while len(beatles) > 3:
    del beatles[-1]
print("Krok 4:", beatles)

# Krok 5
beatles.insert(0, "Ringo Starr")
print("Krok 5:", beatles)

# Sprawdzanie długości listy.
print("The Fab", len(beatles))
