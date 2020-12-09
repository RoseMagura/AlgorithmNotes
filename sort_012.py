def sort_012(input_list):
    output = [None] * len(input_list)
    front_index = 0
    back_index = -1
    ones = 0
    for value in input_list:
        if value == 0:
            output[front_index] = value
            front_index += 1
        elif value == 2:
            output[back_index] = value
            back_index -= 1
        else:
            ones += 1
    for o in output:
        if o is None:
            output[output.index(o)] = 1
    return output

print(sort_012([2, 1, 0, 0, 0, 0]))
# print(sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]))