
with open("09/input.txt") as f:
    input = [[int(num) for num in line.split(',')] for line in f.read().split('\n')]

def calc_area(p1, p2):
    return (abs(p1[0]-p2[0]) + 1) * (abs(p1[1]-p2[1]) + 1)

print(max(calc_area(input[i], input[j]) for i in range(len(input)) for j in range(i + 1, len(input))))
