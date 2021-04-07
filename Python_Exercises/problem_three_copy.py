import sys, collections
from heapq import heapify, heappush, heappop

class Node:
    def __init__(self, value, char = None):
        self.char = char
        self.value = value
        self.left = None
        self.right = None
# add set_value and get_value functions
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value
    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None

    def __repr__(self):
        return f"Node({self.get_value()})"

class Queue():
    def __init__(self):
        self.q = collections.deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    def empty(self):
        return self.__len__() == 0
class Tree():
    def __init__(self, node):
        self.root = node
        
    def set_root(self, node):
        self.root = node
        
    def get_root(self):
        return self.root
    
    def compare(self, node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node 
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1
    
    def insert(self, new_value):
        new_node = new_value
        current_node = self.get_root()

        if current_node == None:
            self.root = new_node
            return

        else:
            while current_node:
                print('NEW NODE', str(new_node))
                comparision = self.compare(current_node, new_node)  
                print(current_node.has_left_child() is False and current_node.has_right_child() is False) 
                if current_node.has_left_child() is False and current_node.has_right_child() is False:
                    if (current_node.value / 2) < new_node.value:
                        current_node.set_right_child(new_node)
                        return
                print(comparision)
                if comparision == -1:
                    if current_node.has_left_child() is False:
                        print('setting left child')
                        current_node.set_left_child(new_node)
                        return
                    else:
                        current_node = current_node.get_left_child()
                elif comparision == 1:
                    if current_node.has_right_child() is False:
                        current_node.set_right_child(new_node)
                        return
                    else:
                        current_node = current_node.get_right_child()
    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node) 
            else:
                s += "\n" + str(node)
                previous_level = level        
        return s

def find_char_freq(string):
    return collections.Counter(string)

def create_heap(data):
    heap = []
    heapify(heap)
    for key, value in data.items():
        heappush(heap, Node(value, key))
    return heap

def get_key(val, d):
        for key, value in d.items():
            if val == value:
                return key

def huffman_encoding(data):
    chars = find_char_freq(data)
    heap = create_heap(chars)
    leaves = []
    prev = None
    key_list = list(chars.keys())
    value_list = list(chars.values())
    value_list = sorted(value_list, reverse=True)
    node_values = []

    while len(heap) > 1:
        min1 = heappop(heap)

        node1 = Node(min1)
        min2 = heappop(heap)

        node2 = Node(min2)
        # merge those two 
        new_value = min1 + min2
        parent = Node(new_value)
        parent.set_left_child(node1)
        parent.set_right_child(node2)
        node_values.append(parent)
       
        for value in value_list:
            if value == new_value:
                c = get_key(value, chars)
                if c is not None:
                    node_values.append(Node(value, c))
                    del chars[c]
        # add back to heap
        heappush(heap, new_value) 
    tree = Tree(heap)
    # print(tree.get_root())
    node_values = node_values[::-1]

    # for value in node_values:
    #     print(str(value))
    #     print(value.get_left_child())
    #     print(value.get_right_child())
    #     print(value.char)

    # tree = Tree(node_values.pop(0))
    # print(node_values)
    while len(node_values) > 0:
        target = node_values.pop(0)
    # print(tree.__repr__())
    return

def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    huffman_encoding(a_great_sentence)
    # print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # print ("The content of the data is: {}\n".format(a_great_sentence))

    # encoded_data, tree = huffman_encoding(a_great_sentence)

    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))

    # decoded_data = huffman_decoding(encoded_data, tree)

    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))