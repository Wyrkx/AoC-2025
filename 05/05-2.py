
with open('05/input.txt') as f:
    ranges, _ = f.read().split('\n\n')
    ranges = [[int(x) for x in line.split('-')] for line in ranges.split('\n')]

ranges.sort(key=lambda range: range[0])
range = ranges[0]

total = 0

for start, end in ranges[1:]:
    if start <= range[1] + 1:
        range[1] = max(range[1], end)
    else:
        total += range[1] - range[0] + 1
        range = [start, end]
else:
    total += range[1] - range[0] + 1

print(total)