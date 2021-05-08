# Initize 1D array
arr = [1, 2, 3]

# Initize 1D array to x
n = 5
x = 3
arr1 = [x] * n  # Expect[3, 3, 3, 3, 3]

# Initize 2D array to x
m = n
arr2 = [[x] * n for i in range(m)]  # Expect [3,3,3,3,3] * 5

# # Initize 3D array to x
k = m
arr3 = [[[x] * n for i in range(m)]
        for j in range(k)]  # Expect [3,3,3,3,3] * 5 * 5
