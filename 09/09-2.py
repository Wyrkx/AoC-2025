
with open("09/input.txt") as f:
    input = [[int(num) for num in line.split(',')] for line in f.read().split('\n')]

compressed_x = [[0, 99999]]
compressed_y = [[0, 99999]]

def decompress_coordinate(p):
    x, y = p
    x_idx = bin_search(compressed_x, x)
    y_idx = bin_search(compressed_y, y)

    if compressed_x[x_idx][0] != x or x != compressed_x[x_idx][1]:
        if x < compressed_x[x_idx][1]:
            compressed_x.insert(x_idx + 1, [x + 1, compressed_x[x_idx][1]])
        if x == compressed_x[x_idx][0]:
            compressed_x[x_idx][1] = x
        else:
            compressed_x.insert(x_idx + 1, [x, x])
            compressed_x[x_idx][1] = x - 1

    if compressed_y[y_idx][0] != y or y != compressed_y[y_idx][1]:
        if y < compressed_y[y_idx][1]:
            compressed_y.insert(y_idx + 1, [y + 1, compressed_y[y_idx][1]])
        if y == compressed_y[y_idx][0]:
            compressed_y[y_idx][1] = y
        else:
            compressed_y.insert(y_idx + 1, [y, y])
            compressed_y[y_idx][1] = y - 1
    
def bin_search(arr, val):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid][0] <= val <= arr[mid][1]:
            return mid
        elif arr[mid][0] < val:
            low = mid + 1
        else:
            high = mid - 1
    return low

def calc_area(p1, p2):
    return (abs(p1[0]-p2[0]) + 1) * (abs(p1[1]-p2[1]) + 1)

# generate compressed grid
for p in input:
    decompress_coordinate(p)

grid = [['.' for _ in range(len(compressed_y))] for _ in range(len(compressed_x))]

for red1, red2 in zip(input, input[1:] + input[0:1]):
    x1_idx = bin_search(compressed_x, red1[0])
    y1_idx = bin_search(compressed_y, red1[1])
    x2_idx = bin_search(compressed_x, red2[0])
    y2_idx = bin_search(compressed_y, red2[1])

    for i in range(min(x1_idx, x2_idx), max(x1_idx, x2_idx) + 1):
        for j in range(min(y1_idx, y2_idx), max(y1_idx, y2_idx) + 1):
            grid[i][j] = 'X'
    
    grid[x1_idx][y1_idx] = '#'
    grid[x2_idx][y2_idx] = '#'


points = []

# find starting point
for i, row in enumerate(grid):
    for j in range(len(row) - 1):
        if row[j] in '#X':
            if row[j + 1] == '.':
                points.append((i, j + 1))
            break
    else:
        continue

    if len(points) > 0:
        break
else:
    raise Exception("No starting point found")

# flood fill
while len(points) > 0:
    x, y = points.pop()
    if grid[x][y] == '.':
        grid[x][y] = 'O'
        if x > 0:
            points.append((x - 1, y))
        if x < len(grid) - 1:
            points.append((x + 1, y))
        if y > 0:
            points.append((x, y - 1))
        if y < len(grid[0]) - 1:
            points.append((x, y + 1))

max_area = 0

# check for rectangles
for red1, red2 in [(input[i], input[j]) for i in range(len(input)) for j in range(i + 1, len(input))]:
    x1_idx = bin_search(compressed_x, red1[0])
    x2_idx = bin_search(compressed_x, red2[0])
    y1_idx = bin_search(compressed_y, red1[1])
    y2_idx = bin_search(compressed_y, red2[1])

    for i in range(min(x1_idx, x2_idx), max(x1_idx, x2_idx) + 1):
        for j in range(min(y1_idx, y2_idx), max(y1_idx, y2_idx) + 1):
            if grid[i][j] == '.':
                break
        else:
            continue
        break
    else:
        max_area = max(max_area, calc_area(red1, red2))
    

with open("09/output.txt", "w") as f:
    f.write('\n'.join(''.join(row) for row in grid))
    f.close()

print(max_area)
