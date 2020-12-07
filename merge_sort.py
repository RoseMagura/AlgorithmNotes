def mergesort(items):
    # Base case, a list of 0 or 1 items is already sorted
    if len(items) <= 1:
        return items
    
    # Otherwise, find the midpoint and split the list
    # TODO
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
    # TODO
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1
    
    merged+= left[left_index:]
    merged+= right[right_index:]

    return merged

merged = merge([1,3,7], [2,5,6])
print(merged)