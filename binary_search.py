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
            array = array[half :]
            length = len(array)
            index += half
            if length == 1 and target != checking:
                return -1
        else:
            array = array[:half]
            length = len(array)
    return -1

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
test_function(test_case)

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 100
index = -1
test_case = [array, target, index]
test_function(test_case) 