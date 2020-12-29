def lps(input_string):

    # TODO: Complete this implementation of the LPS function
    # The function should return one value: the LPS length for the given input string
    length = len(input_string)
    lookup_table = [[0 for x in range(length)] for x in range(length)]

    for i in range(length):
        lookup_table[i][i] = 1

    for s_size in range(2, length+1):
        for start_idx in range(length-s_size+1):
            end_idx = start_idx + s_size - 1
            if s_size == 2 and input_string[start_idx] == input_string[end_idx]:
                # match with a substring of length 2
                lookup_table[start_idx][end_idx] = 2
            elif input_string[start_idx] == input_string[end_idx]:
                # general match case
                lookup_table[start_idx][end_idx] = lookup_table[start_idx+1][end_idx-1] + 2
            else:
                # no match case, taking the max of two values
                lookup_table[start_idx][end_idx] = max(
                    lookup_table[start_idx][end_idx-1], lookup_table[start_idx+1][end_idx])

    # debug line
    # pp.pprint(L)

    return lookup_table[0][length-1]  # value in top right corner of matrix


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
