print("\na)")


def bubble_sort(liste):
    unsorted = 1
    while unsorted:
        unsorted = 0
        for x in range(0, len(liste) - 1):
            if liste[x] > liste[x + 1]:
                liste[x], liste[x + 1] = liste[x + 1], liste[x]
                unsorted = 1
    return liste


liste1 = [9, 1, 34, 7, 2, 3, 45, 6, 78, 56, 36, 65, 33, 21, 23, 34, 45, 6]
print(bubble_sort(liste1))


print("\nb)")


def selection_sort(unsorted):
    sorted = [0 for x in range(0, len(unsorted))]
    for x in range(1, len(unsorted) + 1):
        pos = unsorted.index(max(unsorted))
        sorted[-x] = unsorted[pos]
        unsorted.pop(pos)
    return sorted


liste = [9, 1, 34, 7, 2, 3, 45, 6, 78, 56, 36, 65, 33, 21, 23, 34, 45, 6]
print(selection_sort(liste))