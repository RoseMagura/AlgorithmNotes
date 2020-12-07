def count_inversions(arr):
    inversions = 0
    for i in range(len(arr) - 1):
        rest = arr[(i + 1):]
        # print('COMPARING', str(arr[i]), 'TO REST', str(rest))
        for j in range(len(rest)):
            if rest[j] < arr[i]:
                inversions += 1
    return inversions
    
print(count_inversions([0, 1])) # Expect 0 
print(count_inversions([2, 1])) # Expect 1
print(count_inversions([3, 1, 2, 4])) # Expect 2
print(count_inversions([7, 5, 3, 1])) # Expect 6

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    if count_inversions(arr) == solution:
        print("Pass")
    else:
        print("Fail")

arr = [2, 5, 1, 3, 4]
solution = 4
test_case = [arr, solution]
test_function(test_case)

arr = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
solution = 26
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
solution = 2
test_case = [arr, solution]
test_function(test_case)