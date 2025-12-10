
with open('05/input.txt') as f:
    ranges, fruits = f.read().split('\n\n')
    ranges = [[int(x) for x in line.split('-')] for line in ranges.split('\n')]
    fruits = [int(fruit) for fruit in fruits.split('\n')]

ranges.sort(key=lambda range: range[0])
combined_ranges = [ranges[0]]

for start, end in ranges[1:]:
    if start <= combined_ranges[-1][1] + 1:
        combined_ranges[-1][1] = max(combined_ranges[-1][1], end)
    else:
        combined_ranges.append([start, end])

total = 0
for fruit in fruits:
    for start, end in combined_ranges:
        if start <= fruit <= end:
            total += 1
            break

print(total)