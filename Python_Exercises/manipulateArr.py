"""
Array Manipulation
Given an array of positive integers, replace every element with the least
greater element to its right. If there is no greater element to its right, 
replace it with -1. Return a new array, do not simply modify the original 
array.

Examples:

input: [8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28]
output: [18, 63, 80, 25, 32, 43, 80, 93, 80, 25, 93, -1, 28, -1, -1]
"""

def manipulateArr(myList):
  newArr = []
  for i in range(len(myList)):
    current = myList[i]
    leastGreatest = None
    for j in range(i + 1, len(myList)):
        # print(myList[i], myList[j])
        checking = myList[j]
        if leastGreatest is None:
            if checking > current:
                leastGreatest = checking
            else:
                continue
        if (checking > current and checking < leastGreatest):
            leastGreatest = checking
    
    newArr.append(leastGreatest or -1)
  return newArr

output = manipulateArr([0, 5, 1, 3, 2, 9, 7, 6, 4])
assert output == [1, 6, 2, 4, 4, -1, -1, -1, -1]

input = [8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28]
output = manipulateArr(input)
assert output == [18, 63, 80, 25, 32, 43, 80, 93, 80, 25, 93, -1, 28, -1, -1]

output = manipulateArr([1, 2, 3])
assert output == [2, 3, -1]