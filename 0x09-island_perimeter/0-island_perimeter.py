#!/usr/bin/python3
"""
Calculating the perimeter of a island in a 2D grid
"""


def perimeter_check(grid, x, y):
    """
    Computing the perimeter of unit of land mass
    """
    perimeter = 0
    if grid[x][y - 1] == 0:
        perimeter += 1

    if grid[x][y + 1] == 0:
        perimeter += 1

    if grid[x + 1][y] == 0:
        perimeter += 1

    if grid[x - 1][y] == 0:
        perimeter += 1

    return perimeter


def island_perimeter(grid):
    """
    The main function to calculate perimeter
    """
    perimeter = 0
    isle_x = len(grid[0]) - 1
    isle_y = len(grid) - 1

    for x in range(1, isle_x):
        for y in range(1, isle_y):
            if grid[x][y] == 1:
                perimeter += perimeter_check(grid, x, y)

    return perimeter
