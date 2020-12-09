def fastSelect(arr, k):
    '''TO DO'''
    # Implement the algorithm explained above to find the k^th 
    # largest element in the given array

    limit = len(arr) // 5
    i = 0
    counter = 0
    while counter <= limit:
        cur_list = []
        # for i in range(len(arr) - 1):
        #     print(i)
        #     i += 1
        #     # add to list
        #     cur_list.append(arr[i])
        counter += 1
        print(counter)
        # print(cur_list)
    return

arr = [6, 80, 36, 8, 23, 7, 10, 12, 42]
k = 2
fastSelect(arr, k) # Should be 1
