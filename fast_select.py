def fastSelect(arr, k):
    '''TO DO'''
    # Implement the algorithm explained above to find the k^th 
    # largest element in the given array
    return

def divide(arr):
    print('LENGTH', len(arr))
    section_length = len(arr) // 5
    print(len(arr) % 5)
    # print('SECTION_LENGTH', section_length)
    g1 = arr[:section_length]
    g2 = arr[section_length: (2 * section_length)]
    g3 = arr[(2 * section_length) : (3 * section_length)]
    g4 = arr[(3 * section_length) : (4 * section_length)]
    g5 = arr[(4 * section_length) :]
    print(g1, g2, g3, g4, g5)

arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
k = 2
fastSelect(arr, k) # Should be 1

# TODO: not good for nine
divide([5, 2, 20, 17, 11, 13, 8, 9, 11])
# divide([6, 80, 36, 8, 23, 7, 10, 12, 42, 99])