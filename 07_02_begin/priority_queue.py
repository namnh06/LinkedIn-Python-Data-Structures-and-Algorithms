"""
Python Data Structures - A Game-Based Approach
Priority Queue Class based on heapq.
Robin Andrews - https://compucademy.net/
"""

import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements
    
    def put(self, element, priority):
        heapq.heappush(self.elements, (priority, element))
        
    def get(self):
        return heapq.heappop(self.elements)[1]
    
    def __str__(self):
        return str(self.elements)
    
if __name__ == '__main__':
    pq = PriorityQueue()
    pq.put("A", 6)
    pq.put("B", 5)
    pq.put("C", 2)
    print(pq)
    print(pq.__str__())
    print(pq.get())
    print(pq.__str__())
    print(pq.get())
    print(pq.__str__())