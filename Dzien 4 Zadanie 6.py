print("Witaj!")
imie = list(input("Podaj mi swoje imię: "))
nazwisko = list(input("Podaj mi swoje nazwisko: "))

print("Dziękuję. Twoje imię ma", len(imie), ", a nazwisko", len(nazwisko), "liter.")

for i in range((len(imie)) // 2):
    imie[i], imie[-i - 1] = imie[-i - 1], imie[i]

for i in range((len(nazwisko))//2):
    nazwisko[i], nazwisko[-i-1] = nazwisko[-i-1], nazwisko[i]

print("A tak wyglądałoby twoje imię w lusterku:")
for i in range(len(nazwisko)):
    print(nazwisko[i], end='')
print(" ", end="")
for i in range(len(imie)):
    print(imie[i], end='')
print()
print("Do zobaczenia!")

