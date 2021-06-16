def min_swaps(arr):
    ref_arr = sorted(arr)
    index_dict = {v: i for i,v in enumerate(arr)}
    swaps = 0
    
    for i,v in enumerate(arr):
        correct_value = ref_arr[i]
        if v != correct_value:
            to_swap_ix = index_dict[correct_value]
            arr[to_swap_ix],arr[i] = arr[i], arr[to_swap_ix]
            print(to_swap_ix, i)
            index_dict[v] = to_swap_ix
            index_dict[correct_value] = i
            swaps += 1
    
    return swaps

print(min_swaps([1, 3, 5, 2, 4, 6, 7])) # should print 3
# print(min_swaps([4, 3, 1, 2]))