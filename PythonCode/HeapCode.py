import heapq

# Define
minHeap = [9, 3, 5, 1, 2]
heapq.heapify(minHeap)

maxHeap = [9, 3, 5, 1, 2]
heapq._heapify_max(maxHeap)


# Insertion
heapq.heappush(minHeap, 10)
# heapq doesn't have built in maxHeap .insert
maxHeap.append(10)
heapq._siftdown_max(maxHeap, 0, len(maxHeap) - 1)

# Access
smallest = minHeap[0]
largest = maxHeap[0]


# Deletion
print(heapq.heappop(minHeap))
print(heapq.heappop(maxHeap))
