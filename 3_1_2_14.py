blokow = int(input("Wprowadź liczbę bloków: "))

wysokosc = 0
klocki = 0
while (klocki + wysokosc) < blokow:
    wysokosc += 1
    klocki += wysokosc

print("Wysokość piramidy wynosi:", wysokosc)

