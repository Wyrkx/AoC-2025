import math

def invalid_ids(start: int, end: int) -> int:
    return sum(i for i in range(start, end + 1) if len(str(i)) % 2 == 0 and str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:])

with open('02/input.txt', 'r') as f:
    input = [[int(num) for num in line.strip().split('-')] for line in f.read().split(',') if line.strip() != '']

print(sum(invalid_ids(start, end) for start, end in input))
