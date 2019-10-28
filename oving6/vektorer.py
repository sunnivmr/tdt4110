import random
import math

print("\na)")


# Funksjon som returnerer en random vektor
def make_vec():
    vec = []
    for i in range(3):
        vec.append(random.randint(-10, 10))
    return vec


print(make_vec())

print("\nb)")

vec1 = make_vec()


# Funksjon som printer ut vektoren vakkert
def vector_print(vec, navn):
    print(navn, "=", vec)


vector_print(vec1, "Vektor 1")


print("\nc)")


# Funksjon som skalarmultipliserer en vektor og returnerer en ny vektor
def vector_skalar(vec, skalar):
    nyvec = []
    for i in range(len(vec)):
        nyvec.append(vec[i] * skalar)
    return nyvec


vec2 = vector_skalar(vec1, 3)
vector_print(vec2, "Vektor 2")


print("\nd)")


# Funksjon som regner ut lengden på en vektor
def vector_length(vec):
    len = 0
    for i in vec:
        len += i ** 2
    len = math.sqrt(len)
    return len


vec3 = [1, 4, 3]
print(vector_length(vec3))


print("\ne)")


# Funksjon som returnerer prikkproduktet av to vektorer
def vector_prikk(vec1, vec2):
    res = 0
    if len(vec1) != len(vec2):
        print("Vektorene må ha lik dimensjon")
        return
    else:
        for i in range(len(vec1)):
            res += (vec1[i] * vec2[i])
    return res


vec4 = [1, 4, 3]
vec5 = [2, 3.1, 5]

print("Prikkproduktet av", vec4, "og", vec5, "er:", format(vector_prikk(vec4, vec5), ".3f"))


print("\nf)")


def main():
    vec1 = make_vec()
    vector_print(vec1, "Vektor 1")
    skalar = float(input("Skriv inn en skalar: "))
    nyvec1 = vector_skalar(vec1, skalar)

    print("Lengden før skalering er:", format(vector_length(vec1), ".2f"))
    print("Lengden etter skalering er:", format(vector_length(nyvec1), ".2f"))
    print("Forholden mellom lengden før og etter skalering er:", format(vector_length(nyvec1)/vector_length(vec1), ".2f"))

    prod = vector_prikk(vec1, nyvec1)

    print("Prikkproduktet av", vec1, "og", nyvec1, "er:", prod)


main()
