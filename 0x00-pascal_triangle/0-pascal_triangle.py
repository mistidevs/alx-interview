#!/usr/bin/python3
"""
Using iteration to print the Pascals triangle
"""

def pascal_triangle(n):
  if n <= 0:
    return []
  
  pascals = [[] for _ in range(n)]

  if n >= 1:
    pascals[0].append(1)
  if n >= 2:
    pascals[1].append(1)
    pascals[1].append(1)

  row = 1
  
  if n >= 3:
    for i in range(n - 2):
      pascals[row + 1].append(1)
      
      for j in range(len(pascals[row]) - 1):
        pascals[row + 1].append(pascals[row][j] + pascals[row][j + 1])

      pascals[row + 1].append(1)
      row += 1

  return pascals


if __name__ == "__main__":
  pascal_triangle()
