import numpy as np

with open("input.txt", "r") as f:
    lines = f.readlines()

field = [list(line.strip()) for line in lines]

# lines = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#..."""
# lines = lines.split("\n")
# field = [list(line) for line in lines]

arr = np.array(field)

x, y = np.where(arr == "^")
x, y = x[0], y[0]

rotation = np.array([[0, 1], [-1, 0]])
direction = np.array([-1, 0])


while True:
    arr[x][y] = "X"
    x += direction[0]
    y += direction[1]
    if x in (-1, arr.shape[0]) or y in (-1, arr.shape[1]):
        break
    if arr[x][y] == "#":
        x -= direction[0]
        y -= direction[1]
        direction = rotation @ direction

print(np.count_nonzero(arr == "X"))
