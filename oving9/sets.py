print("\na)")

my_set = set()
print(my_set)

print("\nb)")


def oddetall(set, max):
    for i in range(max):
        if i % 2 != 0:
            set.add(i)


oddetall(my_set, 20)
print(my_set)

print("\nc)")

my_set2 = set()
oddetall(my_set2, 10)
print(my_set2)

print("\nd)")

my_set3 = set()
my_set3 = my_set.difference(my_set2)
print(my_set3)

print("\ne)")
print("Forventer å få {1, 3, 5, 7, 9}:")
print(my_set.intersection(my_set2))
print("\nf)")


def all_unique(lst):
    lst_set = set()
    for i in lst:
        lst_set.add(i)
    if len(lst) == len(lst_set):
        return True
    else:
        return False


print(all_unique([1, 3, 2, 6, 8]))
print(all_unique([1, 3, 5, 2, 3, 7]))

print("\ng)")


def remove_dup(lst):
    lst_set = set()
    new_lst = list()
    for i in lst:
        lst_set.add(i)
    for i in lst_set:
        new_lst.append(i)
    return new_lst


print(remove_dup([1, 3, 5, 2, 3, 7]))

