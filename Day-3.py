test_string = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
''' In this test, the following should be pulled from the string:
    mul(2,4), mul(5, 5), mul(11,8) and mul(8,5)
    I should then run a function which accumulator of the multiplied fingures.
    For example - sum = (2*4) 8 + (5*5) 25 + (11*8) 88 + (8*5) 40 == 161
'''
# Split the sting by the word 'mul'

import re

with open('./Data-Sheets/Advent-of-Code24-Day33.txt', 'r') as file:
    corruptData = file.read()


matches = re.findall(r'mul\((\d+),\s*(\d+)\)', corruptData)

print(matches)
sum = 0
for tup in matches:
    sum += (int(tup[0]) * int(tup[1]))

print(sum)

# Your puzzle answer was 181345830.

# Part Two