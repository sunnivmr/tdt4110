print("a)")

ant = 0
sum  = 0

while ant < 7:
    i = int(input("Skriv inn et heltall:"))
    sum += i
    ant += 1

print("Summen av tallene ble", sum)

summen = 0

#fasit
for i in range(7):
    tall = int(input("Skriv inn et heltall:"))
    summen += tall

print("Summen av tallene ble", summen)

print("\nb)")

i = 0
produkt = 1

while produkt < 1000:
    produkt *= (i + 1)
    i += 1

print("Produktet av tallene ble", produkt)

print("\nc)")

fasit = "Alofi"
spørsmål = "Hva heter hovedstaden til Niue?"
ant = 1

svar = input(spørsmål)

while svar != fasit:
    print("Det var feil, prøv igjen.")
    svar = input(spørsmål)
    ant += 1

print("Korrekt! Du brukte", ant, "forsøk.")