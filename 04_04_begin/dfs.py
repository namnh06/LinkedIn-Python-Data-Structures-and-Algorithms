"""
Python Data Structures - A Game-Based Approach
DFS maze solver.
Robin Andrews - https://compucademy.net/
The stack contains positions as (row, column) tuples. Predecessors are kept in a dictionary.
"""

import os
from helpers import get_path, offsets, is_legal_pos, read_maze
from stack import Stack


def dfs(maze, start, goal):
    s = Stack()
    predecessors = dict({start: None})
    s.push(start)
    
    while not s.is_empty():
        print(s)
        curr = s.pop()
        if curr == goal:
            return get_path(predecessors, start, goal)
        
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neighbor = (curr[0] + row_offset, curr[1] + col_offset)
            if is_legal_pos(maze, neighbor) and neighbor not in predecessors:
                s.push(neighbor)
                predecessors[neighbor] = curr
    
    return None        

if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]


    script_dir = os.path.dirname(__file__)
    # Test 2
    file_path = os.path.join(script_dir,"mazes/mini_maze_dfs.txt")
    maze = read_maze(file_path)
    for row in maze:
        print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]

    # Test 3
    file_path = os.path.join(script_dir,"mazes/mini_maze_dfs.txt")
    maze = read_maze(file_path)
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = dfs(maze, start_pos, goal_pos)
    assert result is None
