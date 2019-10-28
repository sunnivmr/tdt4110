import random

print("a)")

nedre = int(input("Velg en nedre grense: "))
øvre = int(input("Velg en øvre grense: "))



print("b)")

tilfeldig = random.randint(nedre, øvre)
#print("Ditt tilfeldige tall er", tilfeldig)


print("c)")

antforsøk = 1

gjett = int(input("Gjett på tallet: "))
while gjett != tilfeldig:
    if gjett > tilfeldig:
        print("Tallet er lavere")
    elif tilfeldig > gjett:
        print("Tallet er høyere")
    gjett = int(input("Gjett på tallet: "))
    antforsøk += 1


print("Du gjettet riktig!")
print("Du brukte", antforsøk, "forsøk.")