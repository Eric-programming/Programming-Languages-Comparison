# try out the Python queue functions

from collections import deque
# TODO: create a new empty deque object that will function as a queue
quene = deque()

# TODO: add some items to the queue
quene.append(1)
quene.append(2)
quene.append(3)

# TODO: print the queue contents
print(quene)

# TODO: pop an item off the front of the queue
firstVal = quene.popleft()
print(firstVal)
print(quene)
