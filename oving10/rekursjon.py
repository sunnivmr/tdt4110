print("\na)")


# Uten rekursjon
def normal_sum(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum


# Med rekursjon
def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)


print(normal_sum(53))
print(recursive_sum(53))

print("\nb)")


def fakultet(n):
    if n == 0:
        return 1
    return n * fakultet(n - 1)


print(fakultet(5))
print(fakultet(3))

print("\nc)")


def find_smallest_element(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        smallest = find_smallest_element(numbers[1:])
        if numbers[0] < smallest:
            return numbers[0]
        else:
            return smallest


liste = [7, 8, 6, 5, 4, 7, 4, 3, 1, 2, 4, 9]

print(find_smallest_element(liste))

print("\nd)")


#def binary_search(numbers, element):
