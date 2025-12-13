
with open('07/input.txt') as f:
    input = f.read().split('\n')

beams = set([input[0].index("S")])

splits = 0

for row in input[1:]:
    for beam in list(beams):
        if row[beam] == '.':
            continue
        elif row[beam] == '^':
            splits += 1
            beams.remove(beam)
            if beam + 1 < len(row):
                beams.add(beam + 1)
            if beam - 1 >= 0:
                beams.add(beam - 1)
    
print(splits)
