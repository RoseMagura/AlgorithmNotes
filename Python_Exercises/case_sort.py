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

def case_sort_udacity_solution(string):
    upper_ch_index = 0
    lower_ch_index = 0
    
    sorted_string = sorted(string)
    for index, character in enumerate(sorted_string):
        # check if character is lower-case
        ascii_int = ord(character)
        if 97 <= ascii_int <= 122:       # ASCII value of a = 97 & ASCII value of z = 122
            lower_ch_index = index
            break
            
    output = list()
    for character in string:
        ascii_int = ord(character)
        # if character is lower case pick next lower_case character
        if 97 <= ascii_int <= 122:
            output.append(sorted_string[lower_ch_index])
            lower_ch_index += 1
        else:
            output.append(sorted_string[upper_ch_index])
            upper_ch_index += 1
    return "".join(output)

print(case_sort('fedRTSersUXJ') == 'deeJRSfrsTUX')
print(case_sort('defRTSersUXI') == 'deeIRSfrsTUX')
