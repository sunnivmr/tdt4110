from turtle import *
import time


# print("a)")
# # velger farger
# bgc = input("Angi bakgrunnsfarge:")
# c = input("Angi farge på firkant:")
#
# # setter opp tegnevinduet
# setup(330, 330, 0, 0)
# screensize(315, 315)
# goto(-60, 150)
#
# bgcolor(bgc)
# color(c)
#
# # tegner den indre firkanten
# begin_fill()
# right(10)  # tilter den 10 grader nedover
# forward(200)
# right(90)
# forward(200)
# right(90)
# forward(200)
# right(90)
# forward(200)
# end_fill()
#
# time.sleep(10)  # Gjør at vinduet med tegningen ikke lukkes med én gang, men er oppe i 10 sekunder

print("b)")
# velger farger

colormode(255)

print("Angi bakgrunnsfarge")
Rb = int(input("Angi verdi for rødt lys:"))
Gb = int(input("Angi verdi for grønt lys:"))
Bb = int(input("Angi verdi for blått lys:"))

print("Angi firkantfarge")
Rf = int(input("Angi verdi for rødt lys:"))
Gf = int(input("Angi verdi for grønt lys:"))
Bf = int(input("Angi verdi for blått lys:"))

# setter opp tegnevinduet
setup(330, 330, 0, 0)
screensize(315, 315)
goto(-60, 150)

bgcolor(Rb, Gb, Bb)
color(Rf, Gf, Bf)

# tegner den indre firkanten
begin_fill()
right(10)  # tilter den 10 grader nedover
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
end_fill()

time.sleep(10)  # Gjør at vinduet med tegningen ikke lukkes med én gang, men er oppe i 10 sekunder
