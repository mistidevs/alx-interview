#!/usr/bin/python3
"""
Calculating the perimeter of a island in a 2D grid
"""


def perimeter_check(grid, x, y, isle_x, isle_y):
    """
    Validating if cell is valid land
    """
    perimeter = 0
    # Left
    if y == 0 or grid[x][y - 1] == 0:
        perimeter += 1
    # Right
    if y == isle_y - 1 or (y + 1 < len(grid[x]) and grid[x][y + 1] == 0):
        perimeter += 1
    # Bottom
    if x == isle_x - 1 or (x + 1 < len(grid)
                           and y < len(grid[x + 1]) and grid[x + 1][y] == 0):
        perimeter += 1
    # Top
    if x == 0 or (x > 0 and y < len(grid[x - 1]) and grid[x - 1][y] == 0):
        perimeter += 1
    return perimeter


def island_perimeter(grid):
    """
    The main function to calculate perimeter
    """
    if not isinstance(grid, list):
        return 0

    perimeter = 0
    isle_x = len(grid)

    for x in range(0, isle_x):
        isle_y = len(grid[x])
        for y in range(0, isle_y):
            if grid[x][y] == 1:
                perimeter += perimeter_check(grid, x, y, isle_x, isle_y)

    return perimeter
