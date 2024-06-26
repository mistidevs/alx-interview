#!/usr/bin/python3
"""
Calculating the perimeter of a island in a 2D grid
"""


def perimeter_check(grid, x, y, isle_x, isle_y):
    """
    Computing the perimeter of unit of land mass
    """
    perimeter = 0
    # Left
    if grid[x][y - 1] == 0 or y == 0:
        perimeter += 1

    # Right
    if grid[x][y + 1] == 0 or y == isle_y - 1:
        perimeter += 1

    # Bottom
    if grid[x + 1][y] == 0 or x == isle_x - 1:
        perimeter += 1

    # Top
    if grid[x - 1][y] == 0 or x == 0:
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
    isle_y = len(grid[0])

    for x in range(0, isle_x):
        for y in range(0, isle_y):
            if grid[x][y] == 1:
                perimeter += perimeter_check(grid, x, y, isle_x, isle_y)

    return perimeter
