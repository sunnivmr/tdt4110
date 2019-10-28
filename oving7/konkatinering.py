print("\na)")


# Funksjon som printer to stringer etter hverandre
def connect_string(s1, s2):
    print(s1 + " " + s2)


connect_string("James", "Bond")


print("\nb)")

list1 = ["abc", "defg", "hijklm", "nop"]


# Funksjon som printer sammen en liste med stringer
def print_list_string(liste):
    res = ""
    for i in liste:
        res += i
    print(res)


print_list_string(list1)


print("\nc)")

list2 = ["UKA", "lever", "videre"]


# Fuksjon som printer første karakteren i hver string i en liste
def print_first_char(liste):
    for i in liste:
        print(i[0])

print_first_char(list2)


print("\nd)")
print("Kodesnutten vil skrive ut:")
print("BobBob")

