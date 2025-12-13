from functools import reduce

with open('06/input.txt') as f:
    input = zip(*[[op for op in line.split(' ') if op != ''] for line in f.read().split('\n')])

total = 0

for problem in input:
    if problem[-1] == '*':
        total += reduce(lambda x, y: x * int(y), map(int, problem[:-1]), 1)
    elif problem[-1] == '+':
        total += sum(map(int, problem[:-1]))

print(total)
