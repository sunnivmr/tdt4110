print("\na)")


# Funksjon som printer en string bestående av hver fjerde karakter i argumentet
def print_each_four(string):
    res = string[0 : len(string) : 4]
    print(res)


string1 = "I Was Told There’d Be Cake"
print_each_four(string1)


print("\nb)")

list1 = ["sabel", "kan", "mestr", "kuleis"]


# Funksjon som printer ut de to siste karakterene i en liste av stringer
def print_last_two(liste):
    res = ""
    for i in liste:
        res += i[-2:]
    print(res)


print_last_two(list1)


print("\nc)")
streng = "I Want Cake"
streng = streng[-4:100:]
print(streng)