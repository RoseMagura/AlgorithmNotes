def mergesort(items):
    # Base case, a list of 0 or 1 items is already sorted
    if len(items) <= 1:
        return items
    
    # Otherwise, find the midpoint and split the list
    midpoint = len(items) // 2
    left = items[:midpoint]
    right = items[midpoint:]
    
    # Call mergesort recursively with the left and right half
    left = mergesort(left)
    right = mergesort(right)
    
    # Merge our two halves and return
    return merge(left, right)
    
def merge(left, right):
    # Given two ordered lists, merge them together in order,
    # returning the merged list.
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            print('CHANGING', str(left[left_index]), str(right[right_index]))
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged+= left[left_index:]
    merged+= right[right_index:]

    return merged

def count_inversions(arr):
    inversions = 0
    for i in range(len(arr) - 1):
        rest = arr[(i + 1):]
        for j in range(len(rest)):
            if rest[j] < arr[i]:
                inversions += 1
    return inversions
    
# print(count_inversions([0, 1])) # Expect 0 
# print(count_inversions([2, 1])) # Expect 1
# print(count_inversions([3, 1, 2, 4])) # Expect 2
# print(count_inversions([7, 5, 3, 1])) # Expect 6

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    if count_inversions(arr) == solution:
        print("Pass")
    else:
        print("Fail")

arr = [2, 5, 1, 3, 4]
# solution = 4
# test_case = [arr, solution]
# test_function(test_case)
arr = [7, 5, 3, 1]
mergesort(arr)

# arr = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
# solution = 26
# test_case = [arr, solution]
# test_function(test_case)

# arr = [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
# solution = 2
# test_case = [arr, solution]
# test_function(test_case)