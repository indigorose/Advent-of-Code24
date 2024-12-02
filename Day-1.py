from pandas import *

import re

files_data = read_csv("Data-Sheets/Advent-of-Code24-Day1-Sheet - Sheet1.csv", header=None, names=['Column1', 'Column2'],
                      dtype=int)

list_A = files_data['Column1'].tolist()
list_B = files_data['Column2'].tolist()

# Test scripts
x = list_A[0:5]
y = list_B[0:5]

print(x, y)


def dayOnePartOne(lista, listb):
    # Store the final result
    result = 0
    # Loop through list to determine difference and add to result
    for i in range(0, len(lista)):
        if (lista[i] > listb[i]):
            difference = (lista[i] - listb[i])
        else:
            difference = (listb[i]-lista[i])
        # print(difference)
        result += difference

    return result



print(dayOnePartOne(list_A, list_B))

# Estimated result to Day 1 part 1 = 1454450(wrong) - 1873376 - correct

# Part 2

leftList = [1, 4, 8, 3, 9]
rightList = [8, 2, 5, 1, 1]

'''
In this part, the following should happen
1 appears twice = 1*2 = 2
4 appears 0 = 4*0 = 0
8 appears once = 8*1 = 8
3 appears 0 = 3*0 = 0
9 appears 0 = 9*0 = 0
result = 2 + 0 + 8 + 0 + 0 = 10
'''


def dayOnePartTwo(lista, listb):
    # Create a dictionary to hold the keys(list_A values) and values(count of list_A occurrences in list_B)
    list_dict = {}
    for i in range(0, len(lista)):
        list_dict.update({lista[i]: listb.count(lista[i])})

    # Loop through keys and values, multiplying for result
    sum_result = 0
    for k, v in list_dict.items():
        j = k * v
        # print(x)
        sum_result += j
    return sum_result


print(dayOnePartTwo(list_A, list_B))

# Expected result = 18997088 - correct!!
