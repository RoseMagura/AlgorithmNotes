def coin_change(coins, amount):

    # TODO: Complete the coin_change function
    # This should return one value: the fewest coins needed to make up
    # the given amount
    number_coins = 0
    if coins[0] > amount:
        return -1
    while amount:
        current_value = coins.pop(-1)
        remainder = amount % current_value
        if current_value > amount:
            continue
        number_coins += amount // current_value
        if remainder == 0:
            break
        amount = remainder
    return number_coins


def test_function(test_case):
    arr = test_case[0]
    amount = test_case[1]
    solution = test_case[2]
    output = coin_change(arr, amount)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arr = [1, 2, 5]
amount = 11
solution = 3
test_case = [arr, amount, solution]
test_function(test_case)

arr = [1, 4, 5, 6]
amount = 23
solution = 4
test_case = [arr, amount, solution]
test_function(test_case)

arr = [5, 7, 8]
amount = 2
solution = -1
test_case = [arr, amount, solution]
test_function(test_case)
