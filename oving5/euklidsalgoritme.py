
print("a)")


def gcd(a, b):
    original_a = a
    original_b = b
    while b != 0:
        gammel_b = b
        b = a%b
        a = gammel_b
    print("Største felles divisor av",original_a, "og", original_b, "er", a)
    return a


gcd(160, 195)
gcd(89358, 3124)

print("b)")


def reduce_fraction(a, b):
    d = gcd(a, b)
    a = int(a/d)
    b = int(b/d)
    print("Forkortet brøk blir", a, "/", d)
    return a, "/", d


reduce_fraction(5, 10)
reduce_fraction(160, 195)
