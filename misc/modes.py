from collections import Counter

# helper function
def split(str):
    return [char for char in str]

def modes(data):
    chars = split(data)
    freq = Counter(chars)
    final = []
    # if all characters are same frequency
    if(len(Counter(freq.values()).values()) == 1):
        return []
    max_count = max(freq.values())
    for char in freq.keys():
        if(freq[char] == max_count):
            final.append(char)
    
    final.sort()
    return final

assert(modes('tomato') == ['o', 't'])
assert(modes([1, 3, 3, 7]) == [3])
assert(modes(["redder"]) == [])
assert(modes([8, 8, 6, 6, 6, 8]) == [])