"""
Python Data Structures - A Game-Based Approach
Queue class
Robin Andrews - https://compucademy.net/
"""

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()
    
    def enque(self, item):
        self.items.append(item)
        
    def dequeu(self):
        return self.items.popleft()
    
    def peek(self):
        return self.items[0]
    
    def is_empty(self):
        return not self.items
    
    def __string__(self):
        return str(self.items)

if __name__ == '__main__':
    q = Queue()
    q.enque(1)
    print(q.peek())
    q.enque(2)
    print(q.__string__())
    print(q.peek())
    print(q.dequeu())
    print(q.peek())