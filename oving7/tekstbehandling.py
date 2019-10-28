print("\na)")


def blokk_bokstaver(string):
    return string.strip().upper()


print(blokk_bokstaver(" \n The Sky's Awake So I'm Awake  \t  "))


print("\nb)")


def splitt_ord(string, char):
    return string.split(char)


print(splitt_ord("Hakuna Matata", 'a'))


print("\nc)")

s1 = "eat"
s2 = "I want to be like a caterpillar. Eat a lot. Sleep for a while. Wake up beautiful."


def func(s1, s2):
    s = "My bed is a magical place where I suddenly remember everything I forgot to do."
    if s1 in s2.lower():
        s = "The more you weigh, the harder you are to kidnap. Stay safe. Eat cake."
    print(s)


func(s1, s2)

print("\nd)")


def kult(char):
    i = 1
    while i <= 8:
        print(char * i)
        i += 1
    i = 7
    while i >= 1:
        print(char * i)
        i -= 1

kult('Z')

