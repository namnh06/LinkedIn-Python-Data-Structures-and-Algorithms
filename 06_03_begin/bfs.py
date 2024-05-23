"""
Python Data Structures - A Game-Based Approach
BFS maze solver.
Robin Andrews - https://compucademy.net/
The queue contains positions as (row, column) tuples. Predecessors are kept in a dictionary.
"""

import os
from helpers import get_path, offsets, is_legal_pos, read_maze
from queue_ll import Queue


def bfs(maze, start, goal):
    q = Queue()
    q.enqueue(start)
    predecessors = dict({start: None})
    
    while not q.is_empty():
        current_pos = q.dequeue()
        if current_pos == goal:
            return get_path(predecessors, start, goal)
        
        for direction in ["up", "right", "down", "left"]:
            row_pos, col_pos = offsets[direction]
            neighbor = (current_pos[0] + row_pos, current_pos[1] + col_pos)
            if is_legal_pos(maze, neighbor) and neighbor not in predecessors:
                q.enqueue(neighbor)
                predecessors[neighbor] = current_pos

    return None

if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    script_dir = os.path.dirname(__file__)
    # Test 2
    file_path = os.path.join(script_dir,"mazes/mini_maze_bfs.txt")
    maze = read_maze(file_path)
    # for row in maze:
    #     print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

    # Test 3
    file_path = os.path.join(script_dir,"mazes/mini_maze_bfs.txt")
    maze = read_maze(file_path)
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = bfs(maze, start_pos, goal_pos)
    assert result is None
