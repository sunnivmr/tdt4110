print("\na)")


# Funksjon som skriver ut hver karakter i en string
def print_character(string):
    for i in string:
        print(i)


print_character("Hola")


print("\nb)")


def return_third(string):
    try:
        return string[2]
    except IndexError:
        return "q"


print(return_third("Baby"))
print(return_third("Bo"))


print("\nc)")


def return_biggest(string):
    return len(string)-1


print(return_biggest("The Way of Kings"))
print(return_biggest("Elantris"))
