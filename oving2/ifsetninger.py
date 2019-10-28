print("a)")

tid = int(input("Hvor mange minutt har kaken stått i ovnen? "))

if (tid >= 50):
    print("Kaken kan tas ut av ovnen.")

print("Tips til servering: vaniljeis.")

print("b)")

epler = int(input("Hvor mange epler har du? "))
barn = int(input("Hvor mange barn passer du? "))

if (barn > 0):
    print("Da blir det", epler // barn, "epler til hvert barn")
    print("og", epler % barn, "epler til overs til deg selv.")

print("Takk for i dag!")

print("c)")

alder = int(input("Skriv inn din alder:"))
if (alder >= 18):
    print("Du kan stemme:)")
else:
    print("Du kan ikke stemme ennå")

print("d)")

alder = int(input("Skriv inn din alder:"))
if (alder >= 18):
    print("Du kan stemme både ved lokalvalg og Stortingsvalg")
elif (alder >= 16):
    print("Du kan stemme ved lokalvalg, men ikke ved Stortingsvalg")
else:
    print("Du kan ikke stemme ennå")

print("e)")
alder = int(input("Din alder:"))

if (alder >= 67):
    print("Billettpris: 40 kr")
elif (alder >= 26):
    print("Billettpris: 80 kr")
elif (alder >= 12):
    print("Billettpris: 50 kr")
elif (alder >= 3):
    print("Billettpris: 30 kr")
else:
    print("Billetten er gratis")