
def largest_joltage(bank: str):
    batt1 = 0
    batt1_index = -1
    for i in range(len(bank) - 1):
        if int(bank[i]) > batt1:
            batt1 = int(bank[i])
            batt1_index = i
    
    batt2 = 0
    for i in range(batt1_index + 1, len(bank)):
        if int(bank[i]) > batt2:
            batt2 = int(bank[i])
    
    return batt1 * 10 + batt2

with open('03/input.txt', 'r') as f:
    input = [line.strip() for line in f.read().split('\n') if line.strip() != '']

print(sum(largest_joltage(bank) for bank in input))
