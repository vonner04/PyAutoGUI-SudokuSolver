import pyautogui as pg
import numpy as np
import time

grid = []

# Get the grid from the user
while True:
    row = list(input("Row: "))
    ints = []

    for n in row:
        ints.append(int(n))
    grid.append(ints)

    if len(grid) == 9:
        break
    print("Row " + str(len(grid)) + " added.")


def possible(x, y, n):
    # Check if the number is in the row
    for i in range(0, 9):
        if grid[x][i] == n:
            return False

    # Check if the number is in the column
    for i in range(0, 9):
        if grid[i][y] == n:
            return False

    # Check if the number is in the 3x3 subgrid
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    # increment rows
    for i in range(0, 3):
        # increment columns
        for j in range(0, 3):
            if grid[x0 + i][y0 + j] == n:
                return False
    return True


# backtracking algorithm
def solve():
    global grid
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                for n in range(1, 10):
                    if possible(x, y, n):
                        grid[x][y] = n
                        solve()
                        grid[x][y] = 0
                return
    print(grid)
    input("More?")


solve()
