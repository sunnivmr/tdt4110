
print("\na)")

my_family = {}

print("\nb)")


def add_family_member(role, name):
    my_family[role] = name


# add_family_member('mor', 'Ingvild')
# print(my_family)
# add_family_member('far', 'Kai')
# print(my_family)
# add_family_member('søster', 'Frida')
# print(my_family)
# add_family_member('bror', 'Viktor')
# print(my_family)


print("\nc)")


def add_family_member(role, name):
    if role not in my_family.keys():
        my_family[role] = [name]
    else:
        my_family[role].append(name)


add_family_member('mor', 'Ingvild')
print(my_family)
add_family_member('far', 'Kai')
print(my_family)
add_family_member('søster', 'Frida')
print(my_family)
add_family_member('bror', 'Viktor')
print(my_family)
add_family_member('søster', 'Birgithe')
print(my_family)
add_family_member('søster', 'Mildrid')
print(my_family)


print("\nd)")

for role in my_family.keys():
    print("Min", role, "heter", my_family[role][0])
    try:
        for i in range(1, 10):
            print("Min", role, "heter", my_family[role][i])
    except:
        continue

print("\nBedre metode:")

for role in my_family:
    for name in my_family[role]:
        print("Min", role, "heter", name)
