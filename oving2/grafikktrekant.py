import time
from turtle import *

# importerer funksjoner fra turtle
print("Hei, jeg kan tegne en trekant")
vinkel = 0

svar = input("Ønsker du spissen på trekanten opp eller ned? (O/N)")

if (svar.lower() != "n" and svar.lower() != "o"):
    print("Feil input")
elif (svar.lower() == "n"):
    vinkel = - 120
else:
    vinkel = 120

pensize(7)  # sett pennen 7 piksler tykk
pencolor("pink")  # sett pennefargen til rosa
bgcolor("grey")  # sett bakgrunnsfargen grå
fillcolor("purple")  # sett fyllfargen lilla
# Tegner en fylt trekant
begin_fill()
forward(200)  # gå 100 piksler framover
left(vinkel)  # drei 120 grader venstre
forward(200)
left(vinkel)
forward(200)
end_fill()

# Holder vinduet med tegningen åpent i 10 sekunder. Ha dette som siste linje i koden din
time.sleep(10)