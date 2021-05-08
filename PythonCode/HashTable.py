# Define
hm = dict()

# Insertion
key1 = 0
value1 = 0
hm[key1] = value1


# Access
key2 = "key"
value2 = "value"
print(hm[key1])
print(hm.get(key2, value2))

hm[key2] = hm.get(key2, value2)

# Deletion
del hm[key2]

# Contains
print(key2 in hm)

# Iterate
for curKey in hm:
    value = hm[curKey]
    print(value)
