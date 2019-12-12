moja_lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print("Pierwotna lista: ")
print(moja_lista)
tymczasowa_lista = []
for i in range(len(moja_lista)):
    if moja_lista[i] not in tymczasowa_lista:
        tymczasowa_lista.append(moja_lista[i])
moja_lista = tymczasowa_lista
print("Lista tylko z unikalnymi elementami:")
print(moja_lista)