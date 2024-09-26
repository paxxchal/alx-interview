#!/usr/bin/python3
"""
This module defines a function to calculate the perimeter of an island.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented in a grid.
    
    Args:
        grid (list of list of int): A rectangular grid where:
            - 0 represents water
            - 1 represents land
            The grid is rectangular with a width and height not exceeding 100.
    
    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Top neighbor
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Bottom neighbor
                if i == rows - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Left neighbor
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Right neighbor
                if j == cols - 1 or grid[i][j+1] == 0:
                    perimeter += 1
    
    return perimeter
