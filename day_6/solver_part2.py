import numpy as np

# with open("input.txt", "r") as f:
#     lines = f.readlines()

# field = [list(line.strip()) for line in lines]

lines = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
lines = lines.split("\n")
field = [list(line) for line in lines]

arr = np.array(field)

x, y = np.where(arr == "^")
x, y = x[0], y[0]

rotation = np.array([[0, 1], [-1, 0]])
direction = np.array([-1, 0])

loop_counter = 0


def get_dir_symbol(direction):
    if direction[0] == 0:
        return "-"
    else:
        return "|"


dir_symbols = ["-", "|"]

arr[x][y] = get_dir_symbol(direction)

while True:
    x += direction[0]
    y += direction[1]
    if x in (-1, arr.shape[0]) or y in (-1, arr.shape[1]):
        break
    if arr[x][y] == get_dir_symbol(rotation @ direction):
        loop_counter += 1
        arr[x][y] = "+"
    elif arr[x][y] == "#":
        x -= direction[0]
        y -= direction[1]
        direction = rotation @ direction
        arr[x][y] = "+"
        print("a")
    else:
        arr[x][y] = get_dir_symbol(direction)
    print(arr)
# check if in the direction to my right I went already right
print(loop_counter)
