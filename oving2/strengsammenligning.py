print("a)")
a = "druer"
b = "DrUer"

print("Sammenligner",a,"og",b)
if (a.lower() == b.lower()):
    print("Det er samme matvare")
else:
    print("Det er to forskjellige matvarer")

print("b)")
n1 = input("Første navn:")
n2 = input("Andre navn:")
liste = []
liste.append(n1)
liste.append(n2)

print("Under føler navnene i alfabetisk rekkefølge:")
liste.sort()
print(liste[0])
print(liste[1])

print("c)")
print("Kodesnutten vil skrive ut dette til skjerm:")
print("k er større enn b")
print("Los Angeles")
print("New York")
print("druer")