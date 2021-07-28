from queue import Queue, LifoQueue, PriorityQueue
import random

q = Queue()
q2 = LifoQueue()
q3 = PriorityQueue()


numbers = [10, 20, 30, 40, 50]
for n in numbers:
    q.put(n)
    q2.put(n)
    q3.put(((n)*random.randint(2, 6), n))

print(q3)
print(q.get())
print(q2.get())
print("0000000000000000")
while not q3.empty():
    print(q3.get())




