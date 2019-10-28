# #Nøstet løkke
# for x in range(5):
#     for y in range(3):
#         print("Jeg elsker ITGK! ", end=" ")
#     print()
#
# #Enkel løkke
# for x in range(5):
#     print("Jeg elsker ITGK!  Jeg elsker ITGK!  Jeg elsker ITGK!")
#
#
# #Uten løkke
# print((("Jeg elsker ITGK!  "*3) + "\n") * 5)
#
print("a)")

ant_stud = int(input("Hvor mange studenter? "))
ant_emne = int(input("Hvor mange emner? "))

for x in range(ant_stud):
    for y in range(ant_emne):
        studnr = x + 1
        emnenr = y + 1
        print("Stud ", studnr, "elsker Emne ", emnenr, end=" ")
    print()

print("b)")
