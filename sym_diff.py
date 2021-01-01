def sym(total_arr):
    while len(total_arr) >= 2:
        arr_one = total_arr.pop()
        arr_two = total_arr.pop()
        diff = set()
        for value in arr_one:
            if value not in arr_two:
                diff.add(value)
        for value_two in arr_two:
            if value_two not in arr_one:
                diff.add(value_two)
    # if arr3 is not None:
    #     extra = set()
    #     for value_three in arr3:
    #         if value_three not in diff:
    #             extra.add(value_three)
    #         for v in diff:
    #             if v not in arr3:
    #                 extra.add(v)
    #     return extra

    return diff


assert sym([[1, 2, 3], [5, 2, 1, 4]]) == {3, 4, 5}
assert len(sym([[1, 2, 3], [5, 2, 1, 4]])) == 3
assert sym([[1, 2, 3, 3], [5, 2, 1, 4]]) == {3, 4, 5}
assert len(sym([[1, 2, 3, 3], [5, 2, 1, 4]])) == 3
assert sym([[1, 2, 3], [5, 2, 1, 4, 5]]) == {3, 4, 5}
assert len(sym([[1, 2, 3], [5, 2, 1, 4, 5]])) == 3
print(sym([[1, 2, 5], [2, 3, 5], [3, 4, 5]]))
# assert sym([[1, 2, 5], [2, 3, 5], [3, 4, 5]]) == {1, 4, 5}
# assert len(sym([[1, 2, 5], [2, 3, 5], [3, 4, 5]])) == 3
# assert sym([1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5]) == {1, 4, 5}
# assert len(sym([1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5])) == 3
# assert sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3]) == {2, 3, 4, 6, 7}
# assert len(sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3])) == 5
# assert sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]) == {1, 2, 4, 5, 6, 7, 8, 9}
# assert len(sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1])) == 8
