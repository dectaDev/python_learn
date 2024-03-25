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

class amin:
    def __init__(self, x, y):
        self.x = x; self.y = y

    def __add__(self, another):
        return amin(self.x+another.x, self.y+another.y)
    
    def draw(self):
        return f'amin is {self.x}, {self.y}'
    
