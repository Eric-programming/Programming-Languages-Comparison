# List
l1 = [3, 1, 2]
l2 = [{"id": 3}, {"id": 1}, {"id": 2}]


def sortBy(obj): return obj["id"]


# Sort in Ascending
l1.sort()
print(l1)
l2.sort(key=sortBy)
print(l2)

#Sort in descending
l1.sort(reverse=True)
print(l1)
l2.sort(reverse=True, key=sortBy)
print(l2)
