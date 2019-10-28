print("Sjakkbrett")
print("a)")
pos = input("Din posisjon:")
bokstav = pos[0]
tall = int(pos[1])
farge = ""


acefh = ["a","c","e","f","h"]
bdfh = ["b", "d", "f", "h"]


if bokstav > "h" or (tall > 8 or tall < 1):
    print("Feil input. Første tegn må være en bokstav A-H eller a-h. Andre tegn må være et tall 1-8")
elif (bokstav in acefh) and (tall % 2 == 0):
    farge = "Hvit"
    print(farge)
elif (bokstav in bdfh) and (tall % 2 != 0):
    farge = "Hvit"
    print(farge)
else:
    farge = "Svart"
    print(farge)

