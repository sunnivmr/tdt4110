# print("a)")
#
# tall1 = float(input("Skriv inn et flyttall: "))
# tall2 = float(input("Skriv inn enda et flyttall: "))
# tall3 = float(input("Skriv inn et siste flyttall: "))
#
# int1 = int(tall1)
# int2 = int(tall2)
# int3 = int(tall3)
#
# print("Konvertert til heltall blir det ", int1, int2, int3)
#
# int4 = int(input("Skriv inn et heltall: "))
# tall4 = float(int4)
#
# print("Konvertert til flyttall blir det: ", tall4)
#
# print("b)")
#
# navn = input("Skriv inn ditt navn: ")
# print("Hei, " + navn)
# alder = int(input("hvor gammel er du? "))
# prog_alder = int(input("Hvor gammel var du da du begynte å programmere? "))
# ant_aar = alder - prog_alder
# print("Da har du programmert i {} år.".format(ant_aar))
#
# input("Syns du de {} årene har vært givende?".format(ant_aar))
# print("Takk for svar, " + navn + "!")

print("c)")
print("Vennligst gi inn et flyttall med minst 5 siffer både før og etter .")
tall = float(input("Hva er tallet ditt?"))
print("Konvertert til heltall med int():", int(tall))
print("Avrundet til nærmeste heltall:", round(tall))
print("Avrundet til to desimaler:", round(tall, 2))
print("Avrundet til fire desimaler:", round(tall, 4))
print("Avrundet til nærmeste tusen:", int(round(tall, -3)))
print("Heltall fra int() konvertert tilbake til flyttall:", float(int(tall)))

print("d)")
flyttall = float(input("Skriv inn et flyttall:"))
desimaler = int(input("Hvor mange desimaler er ønskelig?"))
print("Tallet du skrev er", flyttall, "og med",desimaler, "desimaler blir det", round(flyttall,desimaler))