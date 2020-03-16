# Bubble sort algorithm


def bubbleSort(dataset):
    # TODO: start with the array length and decrement each time

    print("Current state: ", dataset)
    index = len(dataset)
    while index != 0:
        index -= 1
        for i in range(len(dataset) - 1):
            if (dataset[i] > dataset[i + 1]):
                temp = dataset[i]
                dataset[i] = dataset[i + 1]
                dataset[i + 1] = temp


def main():
    list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    bubbleSort(list1)
    print("Result: ", list1)


if __name__ == "__main__":
    main()
