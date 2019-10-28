#a)
pizzapris = 750
studentrabatt = 0.20
tips = 0.08

#b)
total_utentips = (pizzapris * (1-studentrabatt))
total_medtips = total_utentips + (total_utentips*tips)
print("Den totale summen av middagen blir ", total_medtips, " kr.")

#c)
antall = int(input("Hvor mange deltok på middagen?"))
prisperpers = total_medtips/antall
print("Ettersom dere var",antall, "personer, så må hver person betale", prisperpers, "kroner.")