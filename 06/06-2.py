from functools import reduce

with open('06/input.txt') as f:
    input = [line for line in f.read().split('\n')]
    operators, numbers = input[-1], [''.join(num).strip() for num in zip(*input[:-1])]

total, subtotal = 0, 0
curr_op = ""

for i in range(len(operators)):
    if operators[i] != ' ':
        total += subtotal
        curr_op = operators[i]
        if curr_op == '*':
            subtotal = 1
        elif curr_op == '+':
            subtotal = 0

    if numbers[i] != '':
        num = int(numbers[i])
        if curr_op == '*':
            subtotal *= num
        elif curr_op == '+':
            subtotal += num
    

print(total + subtotal)
