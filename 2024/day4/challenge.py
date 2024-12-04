# # Parse the grid into a dictionary of (y,x):c 
# data = open("data04.txt").readlines()
# H, W = len(data), len(data[0])-1
# grid = {(y,x):data[y][x] for y in range(H) for x in range(W)}

# # Part 1 - Find anything that says 'XMAS'
# TARGET = "XMAS"
# DELTAS = [(dy,dx) for dy in [-1,0,1] for dx in [-1,0,1] if (dx!=0 or dy!=0)]
# count = 0
# for y, x in grid:
#     for dy,dx in DELTAS:
#         candidate = "".join(grid.get((y+dy*i, x+dx*i),"") for i in range(len(TARGET)))
#         count += candidate == TARGET
# print("Part 1:", count)

example_data = open("example.txt").readlines()
data = open("input.txt").readlines()

def get_grid(data):
    height, width = len(data), len(data[0])-1
    grid = {(y,x):data[y][x] for y in range(height) for x in range(width)}
    return grid

####################
# Part 1
####################
def get_xmas(grid):
    target = "XMAS"
    deltas = [(dy,dx) for dy in [-1, 0, 1] for dx in [-1,0,1] if (dx!=0 or dy!=0)]
    result = 0
    for y, x in grid:
        for dy, dx in deltas:
            potential_xmas = "".join(grid.get((y+dy*i, x+dx*i), "") for i in range(len(target)))
            if potential_xmas == target:
                result += 1
    return result

example_grid = get_grid(example_data)
example_value = get_xmas(example_grid)
print(example_value)

grid = get_grid(data)
value = get_xmas(grid)
print(value)

####################
# Part 2
####################
def get_x_mas(grid):
    result = 0
    for y, x in grid:
        if grid[y,x] == "A":
            left_to_right = grid.get((y-1,x-1),"")+grid.get((y+1,x+1),"")
            right_to_left = grid.get((y-1,x+1),"")+grid.get((y+1,x-1),"")
            result += {left_to_right, right_to_left} <= {"MS", "SM"}
    return result

value = get_x_mas(grid)
print(value)
