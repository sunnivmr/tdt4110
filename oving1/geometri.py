print("a)")
r = 5
print("Vi har en sirkel med radius", r)
omkrets = 2 * 3.14 * r
print("Omkretsen er", omkrets)
areal = 3.14 * r ** 2
print("Arealet er", areal)
h = 8
volum = areal * h
print("Sylinder med høyde", h, ": Volumet er",volum)

print("b)")
r = 5
print("Vi har en sirkel med radius", r)
omkrets = 2 * 3.14 * r
print("Omkretsen er", format(omkrets, '.2f'))
areal = 3.14 * r ** 2
print("Arealet er", areal)
h = 8
volum = areal * h
print("Sylinder med høyde", h, ": Volumet er", volum)

print("c)")
print("Det skyldes at flyttall ikke lagres nøyaktig i Python")

print("test")
o = 54.90002
d = 2
print("Tallet", o, "med", d,"desimaler blir", format(o, '.2f'))