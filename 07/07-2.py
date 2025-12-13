
with open('07/input.txt') as f:
    input = f.read().split('\n')

beams = {input[0].index("S"): 1}

for row in input[1:]:
    for beam, paths in list(beams.items()):
        if row[beam] == '.':
            continue
        elif row[beam] == '^':
            beams.pop(beam)
            if beam + 1 < len(row):
                if beam + 1 in beams:
                    beams[beam + 1] += paths
                else:
                    beams[beam + 1] = paths
            if beam - 1 >= 0:
                if beam - 1 in beams:
                    beams[beam - 1] += paths
                else:
                    beams[beam - 1] = paths
 
print(sum(beams.values()))
