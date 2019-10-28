print("a)")

stoff = input("Si et stoff du er i besittelse av:")
#molvekt = int(input("Hva er molvekt i gram for {}?".format(stoff)))
molvekt = int(input("Hva er molvekt i gram for " + stoff + "?"))
gram = int(input("Hvor mange gram vann har du?"))
mol = gram/molvekt
antallmol = mol*6.022e+23
print("Du har ", format(antallmol, '.1e'), " molekyler", stoff)
