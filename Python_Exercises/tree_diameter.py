class Node(object):
        
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    def is_leaf(self):
        return self.has_left_child() == False and self.has_right_child() == False
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"
    
class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root

# create a tree and add some nodes
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))
tree.get_root().get_left_child().set_right_child(Node("e"))

# def diameter_of_binary_tree(root):
#     """
#     :param: root - Root of binary tree
#     TODO: Complete this method and return diameter (int) of binary tree
#     """
#     count = 0
#     lengths = []
#     def traverse(node, count):
#         if node:
#             # print(node)
#             count += 1
#             traverse(node.get_left_child(), count)
#             if(node.is_leaf()):
#                 # print(count)
#                 lengths.append(count)
#                 # print(lengths)
#             traverse(node.get_right_child(), count)
#         else:
#             return lengths
#     traverse(root, count)
#     print(lengths)
#     return sum(lengths)

def diameter_of_binary_tree(root):
    return diameter_of_binary_tree_func(root)[1]
    
def diameter_of_binary_tree_func(root):
    """
    Diameter for a particular BinaryTree Node will be:
        1. Either diameter of left subtree
        2. Or diameter of a right subtree
        3. Sum of left-height and right-height
    :param root:
    :return: [height, diameter]
    """
    
    if root is None:
        return 0, 0
    # else:
    #     print(root.value)
        
    left_height, left_diameter = diameter_of_binary_tree_func(root.left)
    # print(diameter_of_binary_tree_func(root.left))
    # print(diameter_of_binary_tree_func(root.left))
    right_height, right_diameter = diameter_of_binary_tree_func(root.right)

    current_height = max(left_height, right_height) + 1
    print('rh', str(right_height))
    print('lh', str(left_height))
    if root is not None:
        print('value', root.value)
    # print(current_height)
    height_diameter = left_height + right_height
    current_diameter = max(left_diameter, right_diameter, height_diameter)

    return current_height, current_diameter

# print('value of', str(diameter_of_binary_tree(tree.get_root())))
diameter = diameter_of_binary_tree(tree.get_root())
print('diameter', str(diameter))
# print(tree.get_root().get_value())
