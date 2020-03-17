# use a recursive algorithm to find a maximum value


# declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def find_max(items):
    max = items[0]
    for index in range(1, len(items) - 1):
        if (max < items[index]):
            max = items[index]
    return max

    # test the function
print(find_max(items))
