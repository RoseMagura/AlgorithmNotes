def lcs(string_a, string_b):
    len_a = len(string_a) + 1
    len_b = len(string_b) + 1
    matrix = []
    matrix.append([0] * len_a)
    for j in range(len_b - 1):
        values = [0]
        for i in range(len_a - 1):
            substring_a = string_a[:(i + 1)]
            substring_b = string_b[:(j + 1)]
            match = False
            if substring_a[-1] == substring_b[-1]:
                match = True
            if match:
                top_left = matrix[j][i]
                values.append(top_left + 1)
            else:
                top = matrix[j][i + 1]
                left = values[i]
                values.append(max(left, top))
        matrix.append(values)
    return matrix[-1][-1]


def udacity_lcs(string_a, string_b):
    
    # initialize the matrix 
    lookup_table = [[0 for x in range(len(string_b) + 1)] for x in range(len(string_a) + 1)]
    
    # enumerate(str) returns a tuple containing the index and character in each iteration
    for char_a_i, char_a in enumerate(string_a):
        
        for char_b_i, char_b in enumerate(string_b):
            
            # If there is a match, 
            # fill that grid cell with the value to the top-left of that cell plus one
            if char_a == char_b:
                lookup_table[char_a_i + 1][char_b_i + 1] = lookup_table[char_a_i][char_b_i] + 1
                
            # If there is not a match, 
            # take the maximum value from either directly to the left or the top cell
            else:
                lookup_table[char_a_i + 1][char_b_i + 1] = max(
                    lookup_table[char_a_i][char_b_i + 1],
                    lookup_table[char_a_i + 1][char_b_i])

    # the bottom-right cell will hold the non-normalized LCS length value.
    return lookup_table[-1][-1]

'''
The time complexity of the above implementation is dominated by the two nested loops, 
Let the length of string_a and string_b is `n` and `m` respectively. 
This would lead to a time complexity of O(n*m). 
But, in general, we can consider it as O(n*n) instead of O(n*m).
'''    

# Test cell


# Run this cell to see how your function is working
test_A1 = "ABCD"
test_B1 = "BD"

lcs_val1 = lcs(test_A1, test_B1
               )
test_A2 = "WHOWEEKLY"
test_B2 = "HOWONLY"

lcs_val2 = lcs(test_A2, test_B2)

test_A3 = "CATSINSPACETWO"
test_B3 = "DOGSPACEWHO"

lcs_val3 = lcs(test_A3, test_B3)

print('LCS val 1 = ', lcs_val1)
assert lcs_val1 == 2, "Incorrect LCS value."
print('LCS val 2 = ', lcs_val2)
assert lcs_val2 == 5, "Incorrect LCS value."
print('LCS val 3 = ', lcs_val3)
assert lcs_val3 == 7, "Incorrect LCS value."
print('Tests passed!')
