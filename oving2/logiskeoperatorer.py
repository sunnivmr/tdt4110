print("a)")
x = 3
y = 8
z = -3

print("1.")
print(-5 < z and 5 > z)

print("2.")
print(y != 8)

print("3.")
print(x == 8 or y == 8)

print("4.")
print(x > 3 and y < 9)

print("5.")
print((x**2 == 8 or y-z != 5) or x+y == y-z)

print("b)")
print("Gi inn a og b, begge heltall i intervall <40,50> eller <70,90>:")
a = int(input("Verdi for a: "))
b = int(input("Verdi for b: "))

if ((a > 70 and a < 90) or (a > 40 and a < 50) and
    (b > 70 and b < 90) or (b > 40 and b < 50)):
    print("Tallene er begge i gyldige intervall ^u^")
else:
    print("Minst ett av tallene er utenfor et gyldig intervall :(")

print("c)")
print("Hei! Jeg har 10 pannekaker jeg ønsker å dele med deg ^u^")
p = int(input("Hvor mange pannekaker ønsker du? "))

if p > 10 or p < 0:
    print("Beklager, men det er nok ikke mulig")
else:
    r = 10 - p
    print("Da blir det", p, "på deg og", r, "på meg :D")

print("d)")
print("Hei! Jeg har 10 pannekaker jeg ønsker å dele med deg ^u^")
p = int(input("Hvor mange pannekaker ønsker du? "))
s = input("Er du glad i pannekaker? (J/N) ")
elser_pannekaker = False

if s == 'J':
    elsker_pannekaker = True
else:
    elsker_pannekaker = False

if (p > 10 or p < 0) or not elser_pannekaker:
    print("Beklager, men det er nok ikke mulig")
else:
    r = 10 - p
    print("Da blir det", p, "på deg og", r, "på meg :D")
