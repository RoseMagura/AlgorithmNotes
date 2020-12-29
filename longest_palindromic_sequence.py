def lps(input_string): 
    
    # TODO: Complete this implementation of the LPS function
    # The function should return one value: the LPS length for the given input string
    length = len(input_string)
    lookup_table = [[0 for x in range(length)] for x in range(length)]
    for char_i, char in enumerate(input_string):
        for char_j, char2 in enumerate(input_string):
            if(char_i == char_j):
                lookup_table[char_i][char_j] = 1
            if(char == char2):
                if char_i < char_j:
                    print('MATCH with', str(char), str(char2))
                    # print(char_j, char_i)
                    bottom_left = lookup_table[char_i + 1][char_j - 1]
                    print(lookup_table)
                    # lookup_table[char_i][char_j] = bottom_left + 2
                    lookup_table[char_i][char_j] = 100
            else:
                # print('NOT MATCH')
                if char_i < char_j:
                    left = lookup_table[char_i][char_j - 1]
                    bottom = lookup_table[char_i + 1][char_j]
                    lookup_table[char_i][char_j] = max(left, bottom)

    print(lookup_table)
    return 

def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = lps(string)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

lps('NAN')

string = 'BxAoNxAoNxA'
solution = 5
test_case = [string, solution]
# test_function(test_case)

string = 'BANANO'
solution = 3
test_case = [string, solution]
# test_function(test_case)

string = "TACOCAT"
solution = 7
test_case = [string, solution]
# test_function(test_case)