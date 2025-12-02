
with open("01/input.txt", "r") as f:
    input = [line.strip() for line in f.read().split("\n") if line.strip() != ""]

dial = 50
password = 0
dir_map = {'L': -1, 'R': 1}

for line in input:
    delta = dir_map[line[0]] * int(line[1:])
    dial = (dial + delta) % 100
    if dial == 0:
        password += 1

print(password)
