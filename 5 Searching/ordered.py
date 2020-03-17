# searching for an item in an ordered list
# this technique uses a binary search


items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87, 99]


def binarysearch(value, order_list):
    start = 0
    end = len(order_list) - 1
    if (order_list[end] < value or order_list[start] > value):
        return "Value doesn't exist"
    while (start <= end):
        mid = (start + end) // 2
        if (order_list[mid] == value):
            return "The index is %d" % mid
        if (order_list[mid] > value):
            end = mid - 1
        else:
            start = mid + 1


print(binarysearch(23, items))
print(binarysearch(87, items))
print(binarysearch(250, items))
