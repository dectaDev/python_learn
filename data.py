from collections import deque as du
queue = du([])
queue.append(90)
queue.append(91)
queue.append(40)
queue.append(900)
queue.append(903456)
print(queue)

queue.popleft()
print(queue)