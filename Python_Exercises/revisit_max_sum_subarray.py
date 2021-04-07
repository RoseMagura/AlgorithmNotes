# Problem Statement

# You are given an array arr having n integers. 
# You have to find the maximum sum of contiguous subarray among 
# all the possible subarrays. This problem is commonly known as
# Maximum Subarray Problem. Solve this problem in O(nlogn) time, 
# using the Divide and Conquer approach. 

def maxSubArrayRecursive(arr, start, stop):
    if (start == stop):
        return arr[start]
    
    if start < stop:
        mid = (stop + start) // 2
        L = maxSubArrayRecursive(arr, start, mid)
        R = maxSubArrayRecursive(arr, mid+1, stop)
        C = maxCrossingSum(arr, start, mid, stop)
        return max(C, max(L, R))

def maxCrossingSum(arr, start, mid, stop):
    leftSum = arr[mid]
    leftMaxSum = arr[mid]
    
    for i in range(mid-1, start-1, -1):
        leftSum += arr[i]
        if leftSum > leftMaxSum:
            leftMaxSum = leftSum

    rightSum = arr[mid + 1]
    rightMaxSum = arr[mid + 1]
    
    for j in range(mid+2, stop+1):
        rightSum += arr[j]
        if rightSum > rightMaxSum:
            rightMaxSum = rightSum
    return (rightMaxSum + leftMaxSum)

def maxSubArray(arr):
    start = 0
    stop = len(arr) - 1
    return maxSubArrayRecursive(arr, start, stop)

arr = [-2, 7, -6, 3, 1, -4, 5, 7] 
print("Maximum Sum = ",maxSubArray(arr)) # Outputs 13

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
print("Maximum Sum = ",maxSubArray(arr)) # Outputs 6

arr = [-4, 14, -6, 7] 
print("Maximum Sum = ",maxSubArray(arr)) # Outputs 15

arr = [-2, 1, -3, 5, 0, 3, 2, -5, 4]
print("Maximum Sum = ",maxSubArray(arr))  # Outputs 10

arr = [-2, -5, 6, -2, -3, 1, 5, -6]
print("Maximum Sum = ",maxSubArray(arr))  # Outputs 7