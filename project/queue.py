from collections import deque

queue = deque(["Ram","Tarun","Asif","john"])
print(queue)

queue.append("Akbar")
print(queue)

queue.append("Birbal")
print(queue)

print(queue.popleft())
print(queue.popleft())
print(queue)