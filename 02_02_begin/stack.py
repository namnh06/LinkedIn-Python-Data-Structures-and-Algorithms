"""
Python Data Structures - A Game-Based Approach
Stack class
Robin Andrews - https://compucademy.net/
"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items
        # return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
        return None
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
if __name__ == "__main__":
    s = Stack()
    print(s)
    print(s.is_empty())
    s.push(33)
    print(s.is_empty())
    s.push(1)
    print(s)
    print(s.peek())
    print(s.pop())
    s.push(12)
    print(s.__str__())
    print(s.size())