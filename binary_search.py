def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    length = len(array)
    index = 0
    while length > 0:
        checking = array[length // 2]
        half = length // 2
        if target == checking:
            index += half
            return index
        elif target > checking:
            array = array[half:]
            length = len(array)
            index += half
            if length == 1 and target != checking:
                return -1
        else:
            array = array[:half]
            length = len(array)
    return -1


def binary_search_udacity_solution(array, target):
    start_index = 0
    end_index = len(array) - 1

    while start_index <= end_index:
        mid_index = (start_index + end_index)//2

        mid_element = array[mid_index]
        # we have found the element
        if target == mid_element:
            return mid_index
        # the target is less than mid element
        elif target < mid_element:
            # we will only search in the left half
            end_index = mid_index - 1
        # the target is greater than mid element
        else:
            # we will search only in the right half
            start_index = mid_element + 1


def binary_search_recursive(array, target):
    '''Write a function that implements the binary search algorithm using recursion

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    return binary_search_recursive_soln(array, target, 0, len(array) - 1)


def binary_search_recursive_soln(array, target, start_index, end_index):
    if start_index > end_index:
        return -1
    mid_index = (start_index + end_index)//2
    mid_element = array[mid_index]
    if mid_element == target:
        return mid_index
    elif mid_element > target:
        return binary_search_recursive_soln(array, target, start_index, mid_index - 1)
    else:
        return binary_search_recursive_soln(array, target, mid_index + 1, end_index)


def test_function(test_case):
    answer = binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 4
index = 4
test_case = [array, target, index]
test_function(test_case)

array = [1, 2]
target = -20
index = -1
test_case = [array, target, index]
# test_function(test_case)

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 100
index = -1
test_case = [array, target, index]
# test_function(test_case)


def test_function_recursive(test_case):
    answer = binary_search_recursive(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4
index = 4
test_case = [array, target, index]
test_function_recursive(test_case)
