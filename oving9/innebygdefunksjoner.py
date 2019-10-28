print("\na)")

scores = {'Amanda': [88, 92, 100], 'Kennet': [30, 45, 50], 'Einstein': [100,100,100]}

print("\ni)")

print("Dersom vi printer ut scores['Amanda'], vil vi få [88, 92, 100] som output:")
print(scores['Amanda'])

print("\nii)")

print("Dersom vi printer ut scores['Amanda'][2], vil vi få 100 som output:")
print(scores['Amanda'][2])


print("\nb)")

fruits = {}


def add_fruit(fruit):
    if fruit not in fruits.keys():
        fruits[fruit] = 1
    else:
        fruits[fruit] += 1


def remove_fruit(fruit):
    fruits[fruit] -= 1

    if fruits[fruit] == 0:
        del fruits[fruit]


def handletur():
    add_fruit('ananas')
    add_fruit('mango')
    add_fruit('blåbær')
    add_fruit('blåbær')
    add_fruit('mango')
    add_fruit('mango')
    add_fruit('mango')
    add_fruit('bringebær')
    remove_fruit('blåbær')
    remove_fruit('mango')
    add_fruit('persimon')
    remove_fruit('persimon')


def print_kurv():
    for fruit, amount in fruits.items():
        print("Antall", fruit, end="")
        print(":", amount)


handletur()
print_kurv()

print("\nc)")
