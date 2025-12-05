
def largest_joltage(bank: str):
    batts = [0] * 12
    batts_indexes = [-1] * 12

    for batt in range(len(batts)):
        for i in range(0 if batt == 0 else batts_indexes[batt - 1] + 1, len(bank) - (len(batts) - batt - 1)):
            if int(bank[i]) > batts[batt]:
                batts[batt] = int(bank[i])
                batts_indexes[batt] = i
        
    return sum(batt * (10 ** (len(batts) - i - 1)) for i, batt in enumerate(batts))

with open('03/input.txt', 'r') as f:
    input = [line.strip() for line in f.read().split('\n') if line.strip() != '']

print(sum(largest_joltage(bank) for bank in input))
