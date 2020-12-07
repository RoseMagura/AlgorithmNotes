from binary_search import binary_search_recursive

def find_first(arr, number):
    index = binary_search_recursive(arr, number)
    if index is None:
        return None
    while arr[index] == number:
        if index == 0:
            return 0
        if arr[index-1] == number:
            index -= 1
        else:
            return index
    return index

def find_last(arr, number):
    index = binary_search_recursive(arr, number)
    if index is None:
        return None
    while arr[index] == number:
        if index == len(arr) - 1:
            return len(arr) - 1
        if arr[index+1] == number:
            index += 1
        else:
            return index
    return index

def first_and_last_index(arr, number):
    """
    Given a sorted array that may have duplicate values, use binary 
    search to find the first and last indexes of a given value.

    Args:
        arr(list): Sorted array (or Python list) that may have duplicate values
        number(int): Value to search for in the array
    Returns:
        a list containing the first and last indexes of the given value
    """
        
    # TODO: Write your first_and_last function here
    # Note that you may want to write helper functions to find the start 
    # index and the end index
    start = find_first(arr, number)
    end = find_last(arr, number)
    return [start, end]

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(input_list, number)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

input_list = [1]
number = 1
solution = [0, 0]
test_case_1 = [input_list, number, solution]
test_function(test_case_1)

input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number = 3
solution = [3, 6]
test_case_2 = [input_list, number, solution]
test_function(test_case_2)

input_list = [0, 1, 2, 3, 4, 5]
number = 5
solution = [5, 5]
test_case_3 = [input_list, number, solution]
test_function(test_case_3)

input_list = [0, 1, 2, 3, 4, 5]
number = 6
solution = [-1, -1]
test_case_4 = [input_list, number, solution]
test_function(test_case_4)