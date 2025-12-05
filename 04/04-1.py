
def accessible(x: int, y: int, grid: list[str]) -> bool:
    total = 0
    for dx in range(-1, 2):
        x2 = x + dx
        if x2 < 0 or x2 >= len(grid[0]):
            continue
        for dy in range(-1, 2):
            y2 = y + dy
            if y2 < 0 or y2 >= len(grid) or (dx == 0 and dy == 0):
                continue
            if grid[y2][x2] == '@':
                total += 1
                if total >= 4:
                    return False
    return total < 4

with open("04/input.txt", "r") as f:
    input = f.read().split('\n')

print(sum(1 for y in range(len(input)) for x in range(len(input[0])) if input[y][x] == '@' and accessible(x, y, input)))
