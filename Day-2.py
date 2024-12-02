from pandas import *

""" Count the 'safe' levels of a 2D array
 for each 'level' check if the numbers are lower or higher than the next
 and the difference between them is less than three.
 """

# Read the file
# file_data = read_csv('./Data-Sheets/Advent-of-Code24-Day2-Sheet1 - Sheet1.csv', delimiter=r'\s+', header=None)
#
# data_list = file_data.dropna(axis=1, how='all').values.tolist()
#
# print(data_list)

# Reading the file
with open('./Data-Sheets/Advent-of-Code24-Day2-Sheet1 - Sheet1.csv', 'r') as file:
    data_list = [list(map(int, line.split())) for line in file]

# Display the 2D list
print(data_list[0:5])

test_list = [[35, 37, 38, 41, 43, 41], [64, 66, 69, 71, 72, 72], [99, 96, 93, 90, 88]]

""" The result of the test list should be 2 as the last list descends and the rest ascend with a difference of three"""

# Access the sublist of the test list

def dayTwoPartOne(sublist):
    is_ascending = True
    is_descending = True

    for i in range(1, len(sublist)):
        diff = sublist[i] - sublist[i - 1]

        # Check for ascending or descending order
        if diff < 0:
            is_ascending = False  # Breaks ascending condition
        if diff > 0:
            is_descending = False  # Breaks descending condition

        # Check for difference constraint
        if not (1 <= abs(diff) <= 3):
            return False  # Difference constraint violated

    # The sublist passes if it's strictly ascending or descending
    return is_ascending or is_descending


results = [dayTwoPartOne(sublist) for sublist in data_list]
print(results.count(True))
# Estimated answer - 550 (Wrong, too high) - right answer - 524
# Print the results
# for idx, res in enumerate(results):
#     print(f"Sublist {idx + 1}: {'True' if res else 'False'}")

