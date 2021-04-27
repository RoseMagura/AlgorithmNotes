"""
Search
Given a sorted list of integers (0-n, inclusive), and a single integer value 
(0 \le input \le n), find the index of the single integer value in the sorted
list. If the value is not in the list, return -1, otherwise return the index

Examples:

input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10
output: 9

input: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10
output: 10

input: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 22
output: -1
Challenge: perform the search with native language methods, and with loops, 
and with binary search. See this month's readme for more information on binary 
search.
"""

def search(myList, target):
    try:
        return myList.index(target)
    except:
        return -1

def searchWithLoops(myList, target):
    for i in range(len(myList)):
        if myList[i] == target:
            return i
    return -1

def searchWithBinary(myList, target):
    startIndex = (len(myList) - 1) // 2
    currValue = myList[startIndex]
    currIndex = startIndex
    while currValue != target:
        if currValue > target:
            subsection = slice(0, currIndex + 1)
            subList = myList[subsection]
            if currIndex == 1:
                currIndex -= len(subList) // 2
                subsection = slice(0, currIndex + 1)
                subList = myList[subsection]
                if subList[0] == target:
                    return currIndex + 1
                else:
                    return -1
            currIndex -= len(subList) // 2
        else:
            subsection = slice(currIndex + 1, len(myList))
            subList = myList[subsection]
            if len(subList) == 1:
                if subList[0] == target:
                    return currIndex + 1
                else:
                    return -1
            currIndex += len(subList) // 2
        currValue = myList[currIndex]
    return currValue

# Test One
input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10
output = 9

assert search(input, target) == output
assert searchWithLoops(input, target) == output
assert searchWithBinary(input, target) == output

# Test Two
input = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10
output = 10

assert search(input, target) == output
assert searchWithLoops(input, target) == output
assert searchWithBinary(input, target) == output

# Test Three
input = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
target = 22
output = -1

assert search(input, target) == output
assert searchWithLoops(input, target) == output
assert searchWithBinary(input, target) == output

# Test Four
input = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
target = 2
output = 2

assert search(input, target) == output
assert searchWithLoops(input, target) == output
assert searchWithBinary(input, target) == output

# Test Five
input = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
target = 0.5
output = -1

assert search(input, target) == output
assert searchWithLoops(input, target) == output
assert searchWithBinary(input, target) == output