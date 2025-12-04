import math

def invalid_ids(start: int, end: int) -> int:
    return sum(i for i in range(start, end + 1) if is_invalid_id(i))

def is_invalid_id(id: int) -> bool:
    length = len(str(id))
    for factor in find_factors(length):
        if factor == length:
            continue
        if all(str(id)[factor * (i - 1):factor * i] == str(id)[:factor] for i in range(1, length // factor + 1)):
            return True
    return False

def find_factors(n: int) -> list[int]:
    if n == 2:
        return [1, 2]
    factors = []
    
    for i in range(math.ceil(math.sqrt(n)), 0, -1):
        if n % i == 0:
            factors.insert(0, i)
            if i != n // i:
                factors.append(n // i)
    return factors

with open('02/input.txt', 'r') as f:
    input = [[int(num) for num in line.strip().split('-')] for line in f.read().split(',') if line.strip() != '']

print(sum(invalid_ids(start, end) for start, end in input))
