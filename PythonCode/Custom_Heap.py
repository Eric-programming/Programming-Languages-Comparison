import heapq


class MaxHeapObj(object):
    def __init__(self, val): self.val = val
    def __lt__(self, other): return self.val > other.val
    def __eq__(self, other): return self.val == other.val
    def __str__(self): return str(self.val)


class MinHeap(object):
    def __init__(self): self.h = []
    def heappush(self, x): heapq.heappush(self.h, x)
    def heappop(self): return heapq.heappop(self.h)
    def get(self, i): return self.h[i]
    def len(self): return len(self.h)


class MaxHeap(MinHeap):
    def heappush(self, x): heapq.heappush(self.h, MaxHeapObj(x))
    def heappop(self): return heapq.heappop(self.h).val
    def get(self, i): return self.h[i].val

# =================================Testing=======================================


minh = MinHeap()
maxh = MaxHeap()
# add some values
for num in range(5):
    maxh.heappush(num)
    minh.heappush(num)

print(minh.get(0))  # peek
print(maxh.get(0))  # peek

print(minh.heappop())  # pop
print(maxh.heappop())  # pop
