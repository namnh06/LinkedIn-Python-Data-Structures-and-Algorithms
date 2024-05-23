"""
Python Data Structures - A Game-Based Approach
A Star Algorithm maze solver.
Robin Andrews - https://compucademy.net/
Uses a priority queue containing f-values and (i, j) tuples along with dictionaries for
predecessors and g-values.
"""

import os
from helpers import get_path, offsets, is_legal_pos, read_maze
from priority_queue import PriorityQueue


def heuristic(a, b):
    """
    Calculates the Manhattan distance between two pairs of grid coordinates.
    """
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star(maze, start, goal):
    pq = PriorityQueue()
    predecessors = dict({start: None})
    g_values = {start: 0}
    pq.put(start, 1)
    
    while not pq.is_empty():
        current_pos = pq.get()
        if current_pos == goal:
            return get_path(predecessors, start, goal)
        
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neighbor = (current_pos[0] + row_offset, current_pos[1] + col_offset)
            if is_legal_pos(maze, neighbor) and neighbor not in g_values:
                new_cost = g_values[current_pos] + 1
                g_values[neighbor] = new_cost
                f_value = new_cost + heuristic(neighbor, goal)
                pq.put(neighbor, f_value)
                predecessors[neighbor] = current_pos
        
    return None

if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = a_star(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    script_dir = os.path.dirname(__file__)
    # Test 2
    file_path = os.path.join(script_dir,"mazes/mini_maze_bfs.txt")
    maze = read_maze(file_path)
    # for row in maze:
    #     print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = a_star(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

    # Test 3
    file_path = os.path.join(script_dir,"mazes/mini_maze_bfs.txt")
    maze = read_maze(file_path)
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = a_star(maze, start_pos, goal_pos)
    assert result is None
