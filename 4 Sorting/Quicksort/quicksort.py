# Implement a quicksort


items = [20, 6, 8, 53, 56, 23, 87, 41, 49, 19]
# items = [20, 6, 8, 53]


def quickSort(dataset):
    length = len(dataset)  # 4, 1
    if (length < 2):
        return dataset
    else:
        pivotPoint = dataset.pop()  # 53, 8
        lowerArr = []
        highArr = []
        index = 0
        while (index <= len(dataset) - 1):
            if (dataset[index] < pivotPoint):
                lowerArr.append(dataset[index])
            else:
                highArr.append(dataset[index])
            index += 1
        return [*quickSort(lowerArr), pivotPoint, *quickSort(highArr)]


# test the merge sort with data
print(items)
print(quickSort(items))
