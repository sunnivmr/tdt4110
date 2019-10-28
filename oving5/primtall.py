import math

print("a)")


def divisable(a, b):
    if a % b == 0:
        return True
    else:
        return False


print(divisable(10, 3))
print(divisable(10, 5))


print("b)")


def isPrime(a):
    for b in range (2, a):
        if divisable(a, b):
            return False
    return True


print(isPrime(11))
print(isPrime(15))


print("c)")


def isPrimt2(a):
    resb = divisable(a, 2)
    for b in range(1, round(math.sqrt(a) + 0.5), 2):
        if divisable(a, b) and resb:
            return False
    return True


print(isPrime(11))
print(isPrime(15))