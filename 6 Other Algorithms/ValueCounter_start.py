# using a hashtable to count individual items


# define a set of items that we want to count
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# TODO: create a hashtable object to hold the items and counts
counter = {}


# TODO: iterate over each item and increment the count for each one
for value in items:
    if (value in counter.keys()):
        counter[value] += 1
    else:
        counter[value] = 1


# print the results
print(counter)
