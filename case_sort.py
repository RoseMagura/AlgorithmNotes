def case_sort(string):
    """
    Here are some pointers on how the function should work:
    1. Sort the string
    2. Create an empty output list
    3. Iterate over original string
        if the character is lower-case:
            pick lower-case character from sorted string to place in output list
        else:
            pick upper-case character from sorted string to place in output list
    
    Note: You can use Python's inbuilt ord() function to find the ASCII value of a character
    """
    new_string = sorted(string)
    sorted_lower = list()
    sorted_upper = list()
    for char in new_string:
        if char.islower():
            sorted_lower.append(char)
        else:
            sorted_upper.append(char)

    output = ''
    lower_index = 0
    upper_index = 0
    for char in string:
        if char.islower():
            output += sorted_lower[lower_index]
            lower_index += 1
        else:
            output += sorted_upper[upper_index]
            upper_index += 1
    return output

print(case_sort('fedRTSersUXJ') == 'deeJRSfrsTUX')