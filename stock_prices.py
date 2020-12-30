def max_returns(prices):
    """
    Calculate maxiumum possible return

    Args:
       prices(array): array of prices
    Returns:
       int: The maximum profit possible
    """
    min_price_value = float('inf')
    max_price_value = 0
    min_price_index = None
    max_price_index = None

    for i in range(len(prices)):
        if(prices[i] < min_price_value):
            min_price_value = prices[i]
            min_price_index = i
        if(prices[i] > max_price_value):
            max_price_value = prices[i]
            max_price_index = i

    # print('MIN', str(min_price_index), str(min_price_value))
    # print('MAX', str(max_price_index), str(max_price_value))
    if max_price_index < min_price_index:
        return 0

    return max_price_value - min_price_value


prices = [3, 4, 7, 8, 6]
# print(max_returns(prices))

# Test Cases


def test_function(test_case):
    prices = test_case[0]
    solution = test_case[1]
    output = max_returns(prices)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


prices = [2, 2, 7, 9, 9, 12, 18, 23, 34, 37, 45, 54, 78]
solution = 76
test_case = [prices, solution]
# test_function(test_case)

prices = [54, 18, 37, 9, 11, 48, 23, 1, 7, 34, 2, 45, 67]
solution = 66
test_case = [prices, solution]
# test_function(test_case)

prices = [78, 54, 45, 37, 34, 23, 18, 12, 9, 9, 7, 2, 2]
solution = 0
test_case = [prices, solution]
test_function(test_case)
