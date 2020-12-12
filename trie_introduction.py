class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    #     self.root.children = {
    #         'a': {
    #     'd': {
    #         'd': {'word_end': True},
    #         'word_end': False},
    #     'word_end': True},
    # # hi word
    # 'h': {
    #     'i': {'word_end': True},
    #     'word_end': False}}
    
    def add(self, word):
        """
        Add `word` to trie
        """
        while len(word) > 0:
            char = word[0]
            self.root.children[char] = self.recursively_add(word[1:])
        print(self.root.children)
        # trie_words = self.root.children
        # cur_layer = trie_words
        # for char in word:
        #     while char not in cur_layer:
        #         print('not here')
        #         # cur_layer = cur_layer[]
        #         # cur_layer[char] = dict()
        #     # cur_layer = trie_words[char]
        # return trie_words
    
    def recursively_add(self, word):
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
    
    def traverse(self):
        cur_layer = self.root
        for item in cur_layer.children.keys():
            print(cur_layer.children[item])
        return


# word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses'  ,'zebra']
word_trie = Trie()

basic_trie = Trie()

basic_trie.traverse()

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
# word_trie.add('bear')
# print(word_trie.exists('abc'))
