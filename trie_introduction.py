class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        """
        Add `word` to trie
        """
        self.root.children[word[0]] = {
            word[1]: {word[2]: {'word_end': True}, 'word_end': True},
            'word_end': False
        }
        print(self.root.children)
        # word = word[1:]
        # length = len(word)
        # for i in range(length):
        #     word[i]
        return
    
    def exists(self, word):
        """
        Check if word exists in trie
        """
        node = self.root
        for char in word:
            # if char not in node.children:
            #     return False
            node = node.children[char]
            print(node)
        return node['word_end']


# word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses'  ,'zebra']
word_trie = Trie()

# # Add words
# for word in word_list:
#     word_trie.add(word)

# Test words
# test_words = ['bear', 'goo', 'good', 'goos']
# for word in test_words:
#     if word_trie.exists(word):
#         print('"{}" is a word.'.format(word))
#     else:
#         print('"{}" is not a word.'.format(word))

word_trie.add('abc')
print(word_trie.exists('abc'))
