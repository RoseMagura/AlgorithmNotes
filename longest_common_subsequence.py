def lcs(string_a, string_b):
    len_a = len(string_a) + 1
    len_b = len(string_b) + 1
    # print(len_a, len_b)
    matrix = []
    matrix.append([0] * len_a)
    for j in range(len_b - 1):
        # print(j)
        values = [0]
        for i in range(len_a - 1):
            # print('I', str(i))
            # print('matrix so far', str(matrix))
            substring_a = string_a[:(i + 1)]
            substring_b = string_b[:(j + 1)]
            print(substring_a, ',', substring_b)
            match = False
            for char in substring_b:
                for char2 in substring_a:
                    if(char == char2):
                        match = True
            top = matrix[j - 1][i - 1]
            if match:
                print('Match. CHECKING TOP LEFT GRID CELL')
                print(matrix)
                values.append(top + 1)
            else:
                print('Not match. CHECKING LEFT AND TOP CELLS')
                left = matrix[j][i - 1]
                print(max(left, top))
                values.append(max(left, top))

            # values.append(i)
        matrix.append(values)
    print(matrix)
    return 

## Test cell

lcs('ABCD', 'BD')

# Run this cell to see how your function is working
test_A1 = "WHOWEEKLY"
test_B1 = "HOWONLY"

# lcs_val1 = lcs(test_A1, test_B1)

test_A2 = "CATSINSPACETWO"
test_B2 = "DOGSPACEWHO"

# lcs_val2 = lcs(test_A2, test_B2)

# print('LCS val 1 = ', lcs_val1)
# assert lcs_val1==5, "Incorrect LCS value."
# print('LCS val 2 = ', lcs_val2)
# assert lcs_val2==7, "Incorrect LCS value."
# print('Tests passed!')