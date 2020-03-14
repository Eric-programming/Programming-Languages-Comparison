# py Common algorithms

# find greatest common denominator


def GCD(a, b):
    if (a == 0 or b == 0):
        return print("Values must be non-zero ")

    # My solution
    if a > b:
        min = b
    else:
        min = a
    for index in range(1, min + 1):
        if (a % index == 0 and b % index == 0):
            gcdVal = index
    return gcdVal


print(GCD(60, 96))
print(GCD(0, 20))
print(GCD(4, 20))
print(GCD(15, 7))


# Euclidean Algorithm

def GCD_euclidean(a, b):
    while (b != 0):
        t = a
        a = b
        b = t % b

    return a


print(GCD_euclidean(60, 96))
print(GCD_euclidean(96, 60))
print(GCD_euclidean(0, 20))
print(GCD_euclidean(15, 7))
