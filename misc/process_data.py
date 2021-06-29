# You have a two-dimensional list in the following format:

# data = [[2, 5], [3, 4], [8, 7]]

# Each sub-list contains two items, and each item in the sub-lists is an integer.

# Write a function process_data() that processes each sub-list like so:

#     [2, 5] --> 2 - 5 --> -3
#     [3, 4] --> 3 - 4 --> -1
#     [8, 7] --> 8 - 7 --> 1

# and then returns the product of all the processed sub-lists: -3 * -1 * 1 --> 3.

# For input, you can trust that neither the main list nor the sublists will 
# be empty.

def process_data(data):
    diffs = []
    final = 1
    for sublist in data:
        diffs.append(sublist[0] - sublist[1])
    for num in diffs:
        final *= num
    return final 

print(process_data([[2, 9], [2, 4], [7, 5]]) == 28)
print(process_data([[2, 5], [3, 4], [8, 7]]) == 3)