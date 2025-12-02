import math

with open("01/input.txt", "r") as f:
    input = [line.strip() for line in f.read().split("\n") if line.strip() != ""]

print(input)

dial = 50
password = 0
dir_map = {'L': -1, 'R': 1}
prev_zero = False

for line in input:
    print(line, dial, password)
    delta = dir_map[line[0]] * int(line[1:])
    dial = dial + delta

    if dial == 0:
        password += 1
    if dial < 0 and prev_zero:
        password -= 1
    password += abs(math.floor(dial / 100))
    if line[0] == 'L' and dial % 100 == 0 and dial != 0:
        password += 1
    dial = dial % 100
    prev_zero = (dial == 0)

print(password)
