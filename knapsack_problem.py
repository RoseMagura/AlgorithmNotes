# Helper code
import collections

# Naive Approach based on Recursion
def knapsack_max_value(knapsack_max_weight, items):
    lastIndex = len(items) - 1
    return knapsack_recursive(knapsack_max_weight, items, lastIndex)


def knapsack_recursive(capacity, items, lastIndex):
    # Base case
    if (capacity <= 0) or (lastIndex<0):
        return 0
    
    # Put the item in the knapsack
    valueA = 0
    if (items[lastIndex].weight <= capacity):
        valueA = items[lastIndex].value + knapsack_recursive(capacity - items[lastIndex].weight, items, lastIndex - 1)

    
    # Do not put the item in the knapsack
    valueB = knapsack_recursive(capacity, items, lastIndex - 1)
    
    # Pick the maximum of the two results
    result = max(valueA, valueB)
    
    return result

# An item can be represented as a namedtuple
Item = collections.namedtuple('Item', ['weight', 'value'])

def create_lookup_table(knapsack_max_weight, items):
    lookup_table = [0 for _ in range(knapsack_max_weight + 1) ]
    for item in items:
        # replace value if higher
        if lookup_table[item.weight] < item.value:
            lookup_table[item.weight] = item.value
    return lookup_table

def knapsack_max_value(knapsack_max_weight, items):
    """
    Get the maximum value of the knapsack.
    """
    lookup_table = create_lookup_table(knapsack_max_weight, items)
    print(lookup_table)
    capacity = knapsack_max_weight
    knapsack_max_value = lookup_table[knapsack_max_weight]
    for item in items:
        print('CAP', str(capacity))
        if item.weight <= capacity:
            print('can add')
            # do not pick the item
            valueA = knapsack_max_value # no change
            # pick the item
            valueB = item.value + lookup_table[capacity - item.weight]
            capacity -= item.weight
            print('VA', str(valueA), 'VB', str(valueB))
            print(max(valueA, valueB))
            lookup_table[capacity] = max(valueA, valueB)
    print(lookup_table)
    return knapsack_max_value

tests = [
    {
        'correct_output': 14,
        'input':
            {
                'knapsack_max_weight': 15,
                'items': [Item(10, 7), Item(9, 8), Item(5, 6)]}},
    {
        'correct_output': 13,
        'input':
            {
                'knapsack_max_weight': 25,
                'items': [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]}}]
# for test in tests:
#     assert test['correct_output'] == knapsack_max_value(**test['input'])

print(knapsack_max_value(15, [Item(10, 7), Item(9, 8), Item(5, 6)]))